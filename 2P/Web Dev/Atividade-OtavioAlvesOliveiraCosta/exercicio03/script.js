function dia(){
    var dataAtual = new Date()
      var numeroDiaSemana = dataAtual.getDay()
  
  switch (numeroDiaSemana) {
      case 1:
      result.innerHTML = "Hoje é segunda-feira";
      break;
  
      
      case 2:
      result.innerHTML = "Hoje é terça-feira";
      break;
  
      case 3:
      result.innerHTML = "Hoje é quarta-feira";
      break;
  
      
      case 4:
      result.innerHTML = 'Hoje é quinta-feira';
      break;
  
      case 5:
      result.innerHTML = 'Hoje é sexta-feira';
      break;
  
      
      case 6:
      result.innerHTML = 'Hoje é sábado';
      break;
      
      case 7:
      result.innerHTML = 'Hoje é domingo';
      break;
  
      
  } 
  }