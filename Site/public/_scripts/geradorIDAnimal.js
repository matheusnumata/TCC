function gerarId(inputId){
  let input = document.getElementById(inputId);
  let date = new Date();
  let ms = date.getMilliseconds().toString().charAt(0);
  let s = date.getSeconds();
  let m = date.getMinutes();
  let h = date.getHours();
  let ano = date.getFullYear().toString().substr(2,2);

  let id = ano+h+m+s+ms;
  if(id.length == 8)
    id = id + "0";
  if(id.length == 7)
    id = id + "00";

  console.log(id);
  input.value = id;
}
