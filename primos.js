function* primos(){
    let p1 = 2
    while(true){
        yield p1
        p1+=2
    }
}

const primoGenerador = primos()
for(let i=0; i<10; i++){
    console.log(primoGenerador.next().value)
}

