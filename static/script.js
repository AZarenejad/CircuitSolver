let selectedItem = 'Battery';
const elements = ['battery', 'current', 'dependent_voltage', 'dependent_current',
    'capacitor', 'resistor', 'inductor', 'wire'
];


function renderSidebar() {
    console.log("renderSidebar ");
    let sidebar = document.getElementById("sidebar");
    for (i in elements) {
        sidebar.innerHTML += (`<img src="${"./static/img/" + elements[i] + ".png"}"
                                onclick="console.log(selectedItem = '${elements[i]}');
                                createEl(event)"
								class="sidebar-element"
								id="${elements[i]}"
                                />\n`);

    }
}

function createEl(event) {
    let canvas = document.getElementById("canvas");
    let left_pos = Number(prompt("شماره نقطه سمت چپ المان را وارد کنید"));
    let right_pos = Number(prompt("شماره نقطه سمت راست المان را وارد کنید"));
    let value;
    if (selectedItem === 'wire')
    {
        value = 0;
    }
    else
    {
        value = Number(prompt("مقدار المان را وارد کنید"));
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
}

<<<<<<< HEAD
$("#calculate").submit(() => {
    console.log("hereklvhfdn vfi vnf");
=======
$("#node-form").submit(() => {
    console.log("herererererer")
>>>>>>> 235fe1b41831c1476dc9574349447edd2649015d
    $.ajaxSetup({
        async: false
    });
    const prevs = [];
    $.ajax({
        type: 'POST',
        url: '/state/calculate',
        success: (data) => {
            const prevHTML = $("#node-nums").html();
            $("#node-nums").html('<div id="ans">' + data + '</div>' +
                '<button id="reset-btn">Reset</button>');
            console.log('data : ', data);
            prevs.push(prevHTML);
            // setTimeout(()=>{
            // 	$("#ans").html(prevHTML);
            // },5000);
        }
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
