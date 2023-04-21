from flask import Blueprint, jsonify

class Crystal:
    def __init__(self, id, name, color, power):
        self.id = id
        self.name = name
        self.color = color
        self.power = power

crystals = [
    Crystal(1, 'Amethyst', 'Purple', 'Infinite knowledge and wisdom'),
    Crystal(2, 'Tiger\'s Eye', 'Gold', 'Confidence, Strength'),
    Crystal(3, 'Rose Quartz', 'Pink', 'Love')
]

crystal_bp = Blueprint('crystals', __name__, url_prefix = '/crystals')

@crystal_bp.route('', methods = ['GET'])

def handle_crystals():
    crystal_response = []
    for crystal in crystals:
        crystal_response.append({
            'id': crystal.id,
            'name': crystal.name,
            'color': crystal.color,
            'power': crystal.power
        })

    return jsonify(crystal_response)