document.getElementById('symptomForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const symptom = document.getElementById('symptomInput').value;
    // Replace this with actual logic to fetch diseases based on symptom
    const diseases = getDiseases(symptom);
    displayDiseases(diseases);
  });
  
  function getDiseases(symptom) {
    // Dummy function to simulate fetching diseases based on symptom
    switch(symptom.toLowerCase()) {
      case 'headache':
        return ['Migraine', 'Tension headache', 'Cluster headache'];
      case 'fever':
        return ['Flu', 'Common cold', 'Malaria'];
      case 'cough':
        return ['Bronchitis', 'Pneumonia', 'Asthma'];  
      default:
        return ['No diseases found'];
    }
  }
  
  function displayDiseases(diseases) {
    const resultContainer = document.getElementById('result');
    resultContainer.innerHTML = '<h2>Possible Diseases:</h2>';
    if (diseases.length > 0) {
      const ul = document.createElement('ul');
      diseases.forEach(function(disease) {
        const li = document.createElement('li');
        li.textContent = disease;
        ul.appendChild(li);
      });
      resultContainer.appendChild(ul);
    } else {
      resultContainer.innerHTML += '<p>No diseases found</p>';
    }
  }