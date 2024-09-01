// შექმენით for ციკლი რომელიც 20-იდან 50-მდე გამოიტანს ყველა რიცხვს კონსოლში 

for (x=20 ; x<51 ; x++) {
    console.log(x)
} 

//გამოიტანეთ 30-იდან 60-ის ჩათვლით ყველა რიცხვი კონსოლში while ციკლის საშვალებით

let i = 29
while (i < 60) {
    i = i + 1
    console.log(i)
}

//შექმენით ფუნქცია სახელად changeColor რომელიც ფერს შეცვლის div block-ს შესაბამის ღილაკზე დაჭერისას
//დაამატეთ ღილაკები: Red, Blue, Green, Purple, Black

function ChangeColor(color){
    document.getElementById("ColorDiv").style.backgroundColor = color;

}