function sum(str) { //функция для счета суммы чисел
    var sum = 0;
    for (let i = 0; i < str.length; i++) {
        sum += parseInt(str[i])
    }
    return sum;
}

for (let n = 3; n < 10000; n++) { //цикл для обработки n
  let str = `5${"2".repeat(n)}`;
  //console.log(str)
  while (str.includes("52") || str.includes("2222") || str.includes("1122")) { //обработка числа
    if (str.includes("52")) {
    str = str.replace("52", "11");
      //console.log(str)
    }
    if (str.includes("2222")) {
    str = str.replace("2222", "5");
      //console.log(str);
    }
    if (str.includes("1122")) {
    str = str.replace("1122", "25");
      //console.log(str);
    }
  }
  //console.log(sum(str))
  if (sum(str) == 64) { //проверка на сумму чисел
    console.log(n);
  }
}
console.log('Цикл закончен')