let selectedItem = 'Battery';
const elements = ['battery', 'current', 'dependent_voltage', 'dependent_current',
    'capacitor', 'resistor', 'inductor', 'wire'
];


function renderSidebar() {
    console.log("renderSidebar ");
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
    let left_pos = Number(prompt("شماره نقطه سمت چپ المان را وارد کنید"));
    let right_pos = Number(prompt("شماره نقطه سمت راست المان را وارد کنید"));
    let value = 0;
    if (selectedItem != 'wire')
    {
        let value = Number(prompt("مقدار المان را وارد کنید"));
    }
    $.ajaxSetup({
        async: false
    });
    const map = {
        'battery': 'IV',
        'dependent_voltage': 'DV',
        'dependent_current': 'DC',
        'current': 'IC',
        'capacitor': 'C',
        'resistor': 'R',
        'inductor': 'L',
        'wire': 'W'
    };
    const statement = `${map[selectedItem]} ${left_pos} ${right_pos} ${value}`;
    console.log('statement: ', statement)
    $.ajax({
        type: 'POST',
        contentType: 'application/json;charset-utf-08',
        dataType: 'json',
        url: `/state/${statement}`,
        // success: (data, textStatus, jQxhr) => {
        //     if (textStatus == 'success') console.log('successfully sent data and response is: ', data);
        //     else console.error('data: ', data, '\n jQxhr: ', jQxhr);
        // }
    });

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

$("#node-form").submit(() => {
    $.ajaxSetup({
        async: false
    });
    const prevs = [];
    $.ajax({
        type: 'POST',
        url: '/state/calculate',
        // success: (data) => {
        //     const prevHTML = $("#node-nums").html();
        //     $("#node-nums").html('<div id="ans">' + data + '</div>' +
        //         '<button id="reset-btn">Reset</button>');
        //     console.log('data : ', data);
        //     prevs.push(prevHTML);
        //     // setTimeout(()=>{
        //     // 	$("#ans").html(prevHTML);
        //     // },5000);
        // }
    });
    // $("#reset-btn").on('click', () => {
    //     $("#ans").html(prevs[0]);
    //     $(".canvas-element").remove();
    //     $.ajax({
    //         type: 'POST',
    //         url: '/reset'
    //     });
    // });
    // return false;
});
