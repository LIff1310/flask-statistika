from flask import Blueprint, render_template, request
from app.models.statistik_model import hitung_statistik, simpan_data

statistik_bp = Blueprint("statistik", __name__)

@statistik_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data_input = request.form["data"]
        data_angka = list(map(float, data_input.split(",")))

        hasil = hitung_statistik(data_angka)
        simpan_data(data_input, hasil)

        return render_template("hasil.html", hasil=hasil)
    return render_template("index.html")