
function postData(url, data) {
    // Default options are marked with *
    return fetch(url, {
        body: JSON.stringify(data), // must match 'Content-Type' header
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, same-origin, *omit
        headers: {
            'user-agent': 'Example',
            'content-type': 'application/json'
        },
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, cors, *same-origin
        redirect: 'follow', // manual, *follow, error
        referrer: 'no-referrer', // *client, no-referrer
    })
        .then(response => response.json()) // 輸出成 json
}

function predType(result){
    if (result == "unrelated" )
        return("unrelated")
    else if (result == "disagree" )
        return("disagree")
    else
        return("agree")
}




//這邊必須要async funciton 因為python返回需要時間，而JS 又不會block，
//所以需要用async function 加上await去呼叫PY function
async function submit(){ 
    const text1 = document.getElementById('text1').value;
    const text2 = document.getElementById('text2').value;
    const text =text1+text2; 
    //呼叫的方式，就是加上eel.加上剛剛被expose PY function的名稱然後多加()輸入參數，最後加()取值
    result = await eel.predict(text)()  
    
    //最後將返回的值設定在HTML上的<p>內
    document.getElementById('fromPythonText').textContent = result
}

// function submit(){
//     const text1 = document.getElementById('text1').value;
//     const text2 = document.getElementById('text2').value;
    
//     const data = {
//         text1,
//         text2
//     }
    //console.log(data)
    // postData('http://192.168.50.140:80/',data)
    // .then(data=>{
    //     const result = data.result;
    //     console.log(data); 
    //     console.log(result);
    //     print(predType(result));
    //     document.getElementById('textResult').innerHTML = predType(result) 
    // })
    
//}
