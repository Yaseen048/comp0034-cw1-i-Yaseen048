from flask import Blueprint, render_template, flash, redirect, url_for

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/')
def