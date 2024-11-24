document.addEventListener("htmx:afterRequest", (event) => {
  if (event.detail.xhr.status === 200) {
    const response = JSON.parse(event.detail.xhr.responseText);
    if (response.success) {
      const modal = bootstrap.Modal.getInstance(
        docuemnt.getElementById("loginModal")
      );
      modal.hide();
      location.reload();
    } else {
      alert(response.error);
    }
  }
});

document.addEventListener("htmx:afterRequest", (event) => {
  if (event.detail.xhr.status === 200) {
    const response = JSON.parse(event.detail.xhr.responseText);
    if (response.success) {
      // Cierra el modal de registro
      const modal = bootstrap.Modal.getInstance(
        document.getElementById("signupModal")
      );
      modal.hide();
      alert("¡Registro exitoso! Ahora puedes iniciar sesión.");
      location.reload(); // Recarga la página (opcional)
    } else {
      // Maneja los errores y muestra un mensaje
      let errorMessages = Object.values(response.errors).flat().join("\n");
      alert("Errores:\n" + errorMessages);
    }
  }
});
