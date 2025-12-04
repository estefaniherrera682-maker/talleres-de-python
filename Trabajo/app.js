// Cargar usuarios al iniciar
document.addEventListener("DOMContentLoaded", mostrarUsuarios);

// Guardar usuario en LocalStorage
function guardarUsuario() {
    let nombre = document.getElementById("nombre").value;
    let clave = document.getElementById("clave").value;
    let correo = document.getElementById("correo").value;

    if (!nombre || !clave || !correo) {
        alert("Todos los campos son obligatorios");
        return;
    }

    let usuarios = JSON.parse(localStorage.getItem("usuarios")) || [];

    usuarios.push({ nombre, clave, correo });

    localStorage.setItem("usuarios", JSON.stringify(usuarios));

    alert("Usuario registrado correctamente");
    mostrarUsuarios();
}

// Mostrar tabla de usuarios
function mostrarUsuarios() {
    let usuarios = JSON.parse(localStorage.getItem("usuarios")) || [];
    let tabla = document.getElementById("tablaUsuarios");

    tabla.innerHTML = "";

    usuarios.forEach((u, index) => {
        tabla.innerHTML += `
            <tr>
                <td>${u.nombre}</td>
                <td>${u.correo}</td>
                <td>
                    <button onclick="eliminarUsuario(${index})">Eliminar</button>
                </td>
            </tr>
        `;
    });
}

// Eliminar usuario
function eliminarUsuario(i) {
    let usuarios = JSON.parse(localStorage.getItem("usuarios")) || [];
    usuarios.splice(i, 1);
    localStorage.setItem("usuarios", JSON.stringify(usuarios));
    mostrarUsuarios();
}

// Login básico
function login() {
    let nombre = document.getElementById("loginNombre").value;
    let clave = document.getElementById("loginClave").value;

    let usuarios = JSON.parse(localStorage.getItem("usuarios")) || [];

    let existe = usuarios.find(u => u.nombre === nombre && u.clave === clave);

    if (existe) {
        alert("¡Inicio de sesión exitoso!");
    } else {
        alert("Usuario o clave incorrectos");
    }
}
