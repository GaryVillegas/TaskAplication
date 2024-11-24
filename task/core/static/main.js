document.addEventListener("htmx:afterRequest", (event) => {
  if (event.detail.xhr.status === 200) {
    const response = JSON.parse(event.detail.xhr.responseText);
    if (response.success) {
      // Obtén el ID del modal actualmente abierto dinámicamente
      const modalElement = document.querySelector(".modal.show");
      if (modalElement) {
        const modal = bootstrap.Modal.getInstance(modalElement);
        modal.hide();
      }

      // Mensaje de éxito y acción opcional
      if (modalElement.id === "loginModal") {
        alert("¡Inicio de sesión exitoso!");
        location.reload();
      } else if (modalElement.id === "signupModal") {
        alert("¡Registro exitoso! Ahora puedes iniciar sesión.");
        location.reload();
      }
    } else {
      // Maneja errores
      let errorMessages = Object.values(
        response.errors || { error: [response.error] }
      )
        .flat()
        .join("\n");
      alert("Errores:\n" + errorMessages);
    }
  }
});
