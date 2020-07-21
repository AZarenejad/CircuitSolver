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
    let dleft, dright, dtype, a, b;
    if (selectedItem === 'wire')
    {
        value = 0;
    }
    else if (selectedItem === 'dependent_voltage' || selectedItem === 'dependent_current')
    {
        dleft = Number(prompt("شماره نقطه سمت چپ المان به آن وابسته شده را وارد کنید"));
        dright = Number(prompt("شماره نقطه سمت راست المان به آن وابسته شده را وارد کنید"));
        dtype = Number(prompt("تایپ المان به آن وابسته شده را به اینصورت وارد کنید: اگر المان مربوطه از نوع ولتاژ است ، عدد صفر و در غیراینصورت عدد ۱."));
        a = Number(prompt("relation: aX + b. Please enter value of 'a'."));
        b = Number(prompt("relation: aX + b. Please enter value of 'b'."));
        value = 0;
    }
    else
    {
        value = Number(prompt("مقدار المان را وارد کنید"));
        dleft = 0;
        dright = 0;
        dtype = 0;
        a = 0;
        b = 0;
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
    const statement = `${map[selectedItem]} ${left_pos} ${right_pos} ${value} ${dleft} ${dright} ${dtype} ${a} ${b}`;
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

// $("#calculate").submit(() => {
$("#node-form").submit(() => {
    console.log("hereklvhfdn vfi vnf");
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
