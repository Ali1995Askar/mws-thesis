$(document).ready(function () {
    $('#presentationExecution').submit(function (event) {
        let spinnerSpan = document.createElement('span');
        spinnerSpan.classList.add('spinner-border', 'spinner-border-sm');
        spinnerSpan.setAttribute('role', 'status');
        spinnerSpan.setAttribute('aria-hidden', 'true');
        spinnerSpan.setAttribute('id', 'spinnerId');


        var buttonText = document.createTextNode(' Running...');

        let submitButton = document.getElementById("submitButton");
        submitButton.disabled = true;
        submitButton.innerText = "";
        submitButton.appendChild(spinnerSpan);
        submitButton.appendChild(buttonText);

        let data = new FormData();
        data.append("csrfmiddlewaretoken", csrf_token);
        event.preventDefault();
        var form = $(this);
        console.log("==============")
        $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(), // serializes the form's elements.
            success: function (data) {
                submitButton.removeChild(spinnerSpan);
                submitButton.removeChild(buttonText);
                submitButton.innerText = "Generate & Execute";
                submitButton.disabled = false;
                let matchingResults2 = document.getElementById("matchingResults");
                let runTimeResults2 = document.getElementById("runTimeResults");
                console.log(data)
                deleteChild(runTimeResults2);
                deleteChild(matchingResults2);
                fillResults(data.matchingData, data.runTimeData);
            },
        });
    });
});

function deleteChild(elem) {

    let child = elem.lastElementChild;
    while (child) {
        elem.removeChild(child);
        child = elem.lastElementChild;
    }
}


function createActivityItem(algoName, result, textColor) {

    let activityItem = document.createElement('div');
    let iElement = document.createElement('i');
    let activiteLabel = document.createElement('div');
    let strongElement = document.createElement('strong');
    let activityContent = document.createElement('div');

    activiteLabel.classList.add("activite-label");
    activityContent.classList.add("activity-content");
    activiteLabel.classList.add("activite-label");
    activityItem.classList.add("activity-item", "d-flex");
    iElement.classList.add("bi", "bi-circle-fill", "activity-badge", textColor, "align-self-start");


    activityItem.appendChild(activiteLabel);
    activityItem.appendChild(iElement);
    activityItem.appendChild(activityContent);
    activityContent.appendChild(strongElement);

    let algoNameElem = document.createTextNode(algoName);
    let algoResultElem = document.createTextNode(result);

    activiteLabel.appendChild(algoResultElem);
    strongElement.appendChild(algoNameElem);

    return activityItem;
}

function fillResults(orderedAlgoByMatching, orderedAlgoByRunTime) {
    let textColors = [
        'text-light',
        'text-info',
        'text-warning',
        'text-primary',
        'text-danger',
        'text-success',
        'text-muted',
        'text-dark',
    ]
    let activityElem = undefined;
    let matchingResults = document.getElementById("matchingResults");
    let runTimeResults = document.getElementById("runTimeResults");

    for (let i = 0, l = orderedAlgoByMatching.length; i < l; i++) {
        let algName = orderedAlgoByMatching[i].algoName;
        let matchingValue = orderedAlgoByMatching[i].algoMatchingValue;
        let color = textColors[i];
        activityElem = createActivityItem(algName, matchingValue, color);
        matchingResults.appendChild(activityElem);

    }

    activityElem = undefined;
    for (let i = 0, l = orderedAlgoByRunTime.length; i < l; i++) {
        let algName = orderedAlgoByRunTime[i].algoName;
        let matchingValue = orderedAlgoByRunTime[i].algoRunTime;
        let color = textColors[i];
        activityElem = createActivityItem(algName, matchingValue, color);
        runTimeResults.appendChild(activityElem);

    }
}