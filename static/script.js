let selectedItem = 'Battery';
const elements = ['battery', 'current', 'dependent_voltage', 'dependent_current',
    'capacitor', 'resistor', 'inductor'
];

let nodeCount = 0;
let canvasElements = [];

function renderSidebar() {
    let sidebar = document.getElementById("sidebar");
    for (i in elements) {
        sidebar.innerHTML += (`<img src="${"./static/img/" + elements[i] + ".png"}"
								onclick="console.log(selectedItem = '${elements[i]}')"
								class="sidebar-element"
								id="${elements[i]}"
                                />\n`);

    }
}

function createEl(event) {
    let canvas = document.getElementById("canvas");
    // let left = Number(prompt("شماره نقطه سمت چپ المان را وارد کنید"));
    // let right = Number(prompt("شماره نقطه سمت راست المان را وارد کنید"));
    // var value, out;
    // if (selectedItem != "OpAmp") {
    //     value = (selectedItem == "Battery" || selectedItem == "Current") ? (prompt("Please enter this element's equation in the following format\n(m)<sin/cos>((w)t+θ)")) : (Number(prompt("Please enter this element's value")));
    // } else {
    //     out = Number(prompt("Please enter the node connected to the output"));
    // }
    // if (selectedItem == "Battery" || selectedItem == "Current") {
    //     value = (/^\d*$/.test(value)) ? parseFloat(value) : value;
    // }
    // console.log('value: ', value);
    // $.ajaxSetup({
    //     async: false
    // });
    // const map = {
    //     'battery': 'IV',
    //     'dependent_voltage': 'DV',
    //     'dependent_current': 'DC',
    //     'current': 'IC',
    //     'capacitor': 'C',
    //     'resistor': 'R',
    //     'inductor': 'L',

    // };
    // const statement = (selectedItem != "OpAmp") ? `${map[selectedItem]} ${neg} ${pos} ${value}` : `${map[selectedItem]} ${neg} ${pos} ${out}`;
    // console.log('statement: ', statement)
    // $.ajax({
    //     type: 'POST',
    //     contentType: 'application/json;charset-utf-08',
    //     dataType: 'json',
    //     url: `/state/${statement}`,
    //     success: (data, textStatus, jQxhr) => {
    //         if (textStatus == 'success') console.log('successfully sent data and response is: ', data);
    //         else console.error('data: ', data, '\n jQxhr: ', jQxhr);
    //     }
    // });
    // canvasElements.push((selectedItem == "OpAmp") ? { "type": selectedItem, "points": { "neg": neg, "pos": pos, "out": out }, "value": '' } : { "type": selectedItem, "points": { "neg": neg, "pos": pos }, "value": value });


    canvas.innerHTML +=
        (`<div class="canvas-element"
	style="left:${40}px;top:${25}px;">
	<p>${10}</p>  
	<div class="inner-el">
	<p>${1}</p>
	<img class="canvas-img" src="${'./static/img/' + selectedItem + '.png'}">
	<p>${2}</p>
	</div>
    </div>`);
    console.log(canvasElements);
}

// $("#node-form").submit(() => {
//     $.ajaxSetup({
//         async: false
//     });
//     const prevs = [];
//     $.ajax({,
//         type: 'POST',
//         url: '/state/calculate',
//         success: (data) => {
//             const prevHTML = $("#node-nums").html();
//             $("#node-nums").html('<div id="ans">' + data + '</div>' +
//                 '<button id="reset-btn">Reset</button>');
//             console.log('data : ', data);
//             prevs.push(prevHTML);
//             // setTimeout(()=>{
//             // 	$("#ans").html(prevHTML);
//             // },5000);
//         }
//     });
//     $("#reset-btn").on('click', () => {
//         $("#ans").html(prevs[0]);
//         $(".canvas-element").remove();
//         $.ajax({
//             type: 'POST',
//             url: '/reset'
//         });
//     });
//     return false;
// });