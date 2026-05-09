from flask import Blueprint
from flask import jsonify

from app.utils.analytics import (
    calculate_analytics
)

analytics_bp = Blueprint(
    "analytics",
    __name__
)


@analytics_bp.route(
    "/analytics",
    methods=["GET"]
)
def get_analytics():

    analytics = calculate_analytics()

    return jsonify(analytics)