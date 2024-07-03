from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from netflix2.db import get_db

bp = Blueprint('category', __name__, url_prefix='/categorias')


@bp.route('/')
def index():
    db = get_db()
    lista_category = db.execute(
        """SELECT name FROM category """
    ).fetchall()
    pagina = render_template('genero.html', genero = lista_category)

    return pagina