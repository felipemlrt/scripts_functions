// example of javascript code thtat generates fibonacci to the n.
//1 1 2 3 5 8 13 21 34
function fibonacci(limite_de_repeticoes) {
   var anterior_1 = 1, anterior_2 = 1;
   document.write(anterior_1, " ", anterior_2, " ");
   for (i = 0; i < limite_de_repeticoes; i++) {
     atual = anterior_1 + anterior_2;
     document.write(atual, " ");
     anterior_2 = anterior_1;
     anterior_1 = atual;
   }
 }

repeticoes = prompt("Quantas repeticoes da sequencia?")
fibonacci(repeticoes)
