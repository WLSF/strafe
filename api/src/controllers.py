from flask import Blueprint, request, jsonify
from api.src.models import Channel
import logging

logging.basicConfig(level=logging.INFO)
bp = Blueprint('channels', __name__)


@bp.route('/track', methods=['POST'])
def track_channel():
    logging.info('track started')
    channel = request.json['channel']
    response = Channel.track_messages(channel)

    if response:
        return jsonify(message='Tracking'), 200
    else:
        return jsonify(message=response), 400


@bp.route('/messages')
def retrieve_messages_by_time():
    channel = request.args.get('channel', '')
    response = Channel.get_messages_by_time(channel)

    return jsonify(response), 200


@bp.route('/mood')
def retrieve_mood():
    channel = request.args.get('channel', '')
    response = Channel.get_mood_from(channel)

    return jsonify(response), 200
