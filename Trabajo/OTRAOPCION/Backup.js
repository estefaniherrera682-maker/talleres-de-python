document.addEventListener("DOMContentLoaded", cargarBackups);

function crearBackup() {
    let usuarios = JSON.parse(localStorage.getItem("usuarios"));

    if (!usuarios || usuarios.length === 0) {
        alert("No hay usuarios para guardar.");
        return;
    }

    let fecha = new Date().toLocaleString();
    let nombre = "Backup_" + Date.now()

    let backups = JSON.parse(localStorage.getItem("backups")) || [];

    backups.push({
        nombre: nombre,   
        fecha: fecha,
        datos: usuarios
    });

    localStorage.setItem("backups", JSON.stringify(backups));
    alert("Backup creado con éxito.");
    cargarBackups();
}

function cargarBackups() {
    let backups = JSON.parse(localStorage.getItem("backups")) || [];
    let tabla = document.getElementById("tablaBackups");

    tabla.innerHTML = "";

    backups.forEach((b, i) => {
        tabla.innerHTML += `
            <tr>
                <td>${i + 1}</td>
                <td>${b.nombre}</td> 
                <td>${b.fecha}</td>
                <td>
                    <button onclick="descargarBackup(${i})">Descargar</button>
                    <button onclick="eliminarBackup(${i})">Eliminar</button>
                </td>
            </tr>
        `;
    });
}

function descargarBackup(index) {
    let backups = JSON.parse(localStorage.getItem("backups"));
    let backup = backups[index];

    let blob = new Blob([JSON.stringify(backup.datos, null, 2)], { type: "application/json" });
    let enlace = document.createElement("a");

    enlace.href = URL.createObjectURL(blob);
    enlace.download = backup.nombre + ".json";
    enlace.click();
}

function restaurarBackup(index) {
    let backups = JSON.parse(localStorage.getItem("backups"));
    let backup = backups[index];

    if (!confirm("¿Seguro que deseas restaurar este backup? Se reemplazarán todos los usuarios actuales.")) {
        return;
    }

    localStorage.setItem("usuarios", JSON.stringify(backup.datos));
    alert("Usuarios restaurados con éxito.");
}

function eliminarBackup(index) {
    let backups = JSON.parse(localStorage.getItem("backups"));

    if (!confirm("¿Seguro que deseas eliminar este backup?")) {
        return;
    }

    backups.splice(index, 1);
    localStorage.setItem("backups", JSON.stringify(backups));

    cargarBackups();
    alert("Backup eliminado.");
}