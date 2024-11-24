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
