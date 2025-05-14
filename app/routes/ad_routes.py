from flask import Blueprint, request, jsonify
from app.models.ad import Ad
from app.db import SessionLocal

ad_bp = Blueprint("ads", __name__, url_prefix="/ads")

@ad_bp.route("/", methods=["POST"])
def create_ad():
    session = SessionLocal()
    try:
        data = request.get_json()
        ad = Ad(
            title=data["title"],
            description=data.get("description", ""),
            owner=data["owner"]
        )
        session.add(ad)
        session.commit()
        session.refresh(ad)
        return jsonify({"id": ad.id}), 201
    finally:
        session.close()

@ad_bp.route("/<int:ad_id>", methods=["GET"])
def get_ad(ad_id):
    session = SessionLocal()
    try:
        ad = session.get(Ad, ad_id)
        if not ad:
            return jsonify({"error": "Not found"}), 404
        return jsonify({
            "id": ad.id,
            "title": ad.title,
            "description": ad.description,
            "created_at": ad.created_at.isoformat(),
            "owner": ad.owner
        })
    finally:
        session.close()

@ad_bp.route("/<int:ad_id>", methods=["DELETE"])
def delete_ad(ad_id):
    session = SessionLocal()
    try:
        ad = session.get(Ad, ad_id)
        if not ad:
            return jsonify({"error": "Not found"}), 404
        session.delete(ad)
        session.commit()
        return jsonify({"message": "Ad deleted"})
    finally:
        session.close()
