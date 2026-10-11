document.addEventListener("DOMContentLoaded", function() {
    console.log("Mini-Task Manager initialisé avec succès !");

    // Exemple d'interactivité : clic sur une tâche pour afficher un détail ou changer son état visuel
    const taskItems = document.querySelectorAll(".task-item");

    taskItems.forEach(item => {
        item.addEventListener("click", function() {
            // Animation subtile au clic
            this.style.transition = "background-color 0.3s";
            console.log("Vous avez cliqué sur la tâche :", this.querySelector("strong").innerText);
        });
    });
});