from flask import Blueprint, render_template, abort
import json

api = Blueprint('api', __name__)


@api.route('/data')
def show(page):
    return

