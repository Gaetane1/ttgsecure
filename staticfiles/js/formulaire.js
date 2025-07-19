document.addEventListener('DOMContentLoaded', function() {
  // Gestion de la soumission du formulaire de création de compte
  const createAccountForm = document.getElementById('create-account-form');
  if (createAccountForm) {
    createAccountForm.addEventListener('submit', function(e) {
      e.preventDefault();
      
      // Récupération des valeurs
      const nom = document.getElementById('nom').value;
      const email = document.getElementById('email').value;
      const motdepasse = document.getElementById('motdepasse').value;
      
      // Validation simple
      if (nom && email && motdepasse) {
        // Stockage dans localStorage
        const userData = {
          nom,
          email,
          motdepasse
        };
        localStorage.setItem('user_' + email, JSON.stringify(userData));
        
        // Affichage message de succès
        showSubmissionMessage(createAccountForm, 'Compte créé avec succès !', 'success');
        
        // Réinitialisation du formulaire
        createAccountForm.reset();
      } else {
        showSubmissionMessage(createAccountForm, 'Veuillez remplir tous les champs obligatoires', 'error');
      }
    });
  }

  // Gestion de la demande de service
  const serviceRequestForm = document.getElementById('service-request-form');
  if (serviceRequestForm) {
    serviceRequestForm.addEventListener('submit', function(e) {
      e.preventDefault();
      
      const nom = document.getElementById('nom-service').value;
      const service = document.getElementById('service').value;
      const details = document.getElementById('details').value;
      
      if (nom && service) {
        const requestData = {
          nom,
          service,
          details,
          date: new Date().toISOString()
        };
        
        // Stockage des demandes dans un tableau
        let requests = JSON.parse(localStorage.getItem('service_requests')) || [];
        requests.push(requestData);
        localStorage.setItem('service_requests', JSON.stringify(requests));
        
        showSubmissionMessage(serviceRequestForm, 'Demande envoyée avec succès !', 'success');
        serviceRequestForm.reset();
      } else {
        showSubmissionMessage(serviceRequestForm, 'Veuillez remplir les champs obligatoires', 'error');
      }
    });
  }

  // Gestion de la mise à jour de profil
  const updateProfileForm = document.getElementById('update-profile-form');
  if (updateProfileForm) {
    updateProfileForm.addEventListener('submit', function(e) {
      e.preventDefault();
      
      const email = document.getElementById('email-update').value;
      const nom = document.getElementById('nom-update').value;
      const motdepasse = document.getElementById('motdepasse-update').value;
      
      if (email) {
        const userKey = 'user_' + email;
        const userData = JSON.parse(localStorage.getItem(userKey));
        
        if (userData) {
          // Mise à jour des champs modifiés
          if (nom) userData.nom = nom;
          if (motdepasse) userData.motdepasse = motdepasse;
          
          localStorage.setItem(userKey, JSON.stringify(userData));
          showSubmissionMessage(updateProfileForm, 'Profil mis à jour avec succès !', 'success');
          updateProfileForm.reset();
        } else {
          showSubmissionMessage(updateProfileForm, 'Aucun compte trouvé avec cet email', 'error');
        }
      } else {
        showSubmissionMessage(updateProfileForm, 'Veuillez entrer votre email', 'error');
      }
    });
  }

  // Fonction pour afficher les messages de soumission
  function showSubmissionMessage(form, message, type) {
    // Supprime les anciens messages
    const oldMessage = form.querySelector('.submission-message');
    if (oldMessage) oldMessage.remove();
    
    // Crée un nouveau message
    const messageDiv = document.createElement('div');
    messageDiv.className = `submission-message ${type}`;
    messageDiv.textContent = message;
    
    // Ajoute le message après le dernier élément du formulaire
    form.appendChild(messageDiv);
    
    // Affiche le message avec une animation
    setTimeout(() => {
      messageDiv.style.opacity = '1';
      messageDiv.style.transform = 'translateY(0)';
    }, 10);
    
    // Fait disparaître le message après 5 secondes
    setTimeout(() => {
      messageDiv.style.opacity = '0';
      messageDiv.style.transform = 'translateY(-20px)';
      setTimeout(() => messageDiv.remove(), 300);
    }, 5000);
  }

  // Validation en temps réel
  const setupValidation = (input) => {
    input.addEventListener('input', () => {
      if (input.checkValidity()) {
        input.style.borderColor = '#2ecc71';
      } else {
        input.style.borderColor = '#e74c3c';
      }
    });
  };

  // Applique la validation à tous les inputs requis
  document.querySelectorAll('input[required]').forEach(setupValidation);
});