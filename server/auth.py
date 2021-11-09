#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  auth.py
#  
#  Copyright 2021 notna <notna@apparat.org>
#  
#  This file is part of smartledmatrix.
#
#  smartledmatrix is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  smartledmatrix is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with smartledmatrix.  If not, see <http://www.gnu.org/licenses/>.
#

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)
from flask_jwt_extended import create_access_token, set_access_cookies

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        password = request.form["password"]

        if password == current_app.config['PASSWORD']:
            token = create_access_token(identity="admin")

            response = redirect(url_for("index"))
            set_access_cookies(response, token)

            return response
        else:
            flash("Incorrect password!")

    return render_template("auth/login.html")

