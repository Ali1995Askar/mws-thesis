$(document).ready(function () {
    $('#presentationExecution').submit(function (event) {
        event.preventDefault();
        clearResults();
        const submitButton = $("#submitButton");
        disableSubmitButton(submitButton);
        const data = new FormData();
        data.append("csrfmiddlewaretoken", csrf_token);
        $.ajax({
            type: "POST",
            url: url,
            data: $(this).serialize(),
            success:  function (data) {
                 const maxDelay = fillResults(data.matchingData, data.runTimeData);
                 console.log(maxDelay)
                 setTimeout(() => enableSubmitButton(submitButton), maxDelay);

            },
        });
    });

    function disableSubmitButton(button) {
        const spinnerSpan = $('<span>')
            .addClass('spinner-border spinner-border-sm')
            .attr({ role: 'status', 'aria-hidden': 'true', id: 'spinnerId' });

        button.prop('disabled', true)
            .empty()
            .append(spinnerSpan)
            .append(' Running...');
    }

    function enableSubmitButton(button) {
        button.empty().append('Execute').prop('disabled', false);
    }

    function clearResults() {
        $('#matchingResults, #runTimeResults').empty();
    }

    function createActivityItem(algoName, result, textColor) {
        const activityItem = $('<div>').addClass('activity-item d-flex').hide();
        const iElement = $('<i>').addClass(`bi bi-circle-fill activity-badge ${textColor} align-self-start`);
        const activiteLabel = $('<div>').addClass('activite-label').text(result);
        const strongElement = $('<strong>').text(algoName);
        const activityContent = $('<div>').addClass('activity-content').append(strongElement);

        activityItem.append(activiteLabel, iElement, activityContent);

        return activityItem;
    }

    function fillResults(orderedAlgoByMatching, orderedAlgoByRunTime) {
        let maxDelay = 0;

        const textColors = [
            'text-light',
            'text-info',
            'text-warning',
            'text-primary',
            'text-danger',
            'text-success',
            'text-muted',
            'text-dark',
        ];
        const delayValue = 600;
        function appendItemWithDelay(container, algoName, result, textColor, delay) {
            setTimeout(function () {
                const activityElem = createActivityItem(algoName, result, textColor);
                container.append(activityElem);
                activityElem.fadeIn();
            }, delay);
        }

        let matchingContainer = $('#matchingResults');
        let runTimeContainer = $('#runTimeResults');

        for (let i = 0; i < orderedAlgoByMatching.length; i++) {
            const { algoName, algoMatchingValue } = orderedAlgoByMatching[i];
            const color = textColors[i];
            const delay = delayValue * i;
            appendItemWithDelay(matchingContainer, algoName, algoMatchingValue, color, delay);
        }

        for (let i = 0; i < orderedAlgoByRunTime.length; i++) {
            const { algoName, algoRunTime } = orderedAlgoByRunTime[i];
            const color = textColors[i];
            const delay = delayValue * i;
            appendItemWithDelay(runTimeContainer, algoName, algoRunTime, color, delay);
            maxDelay = delay;
        }
        maxDelay = maxDelay + delayValue + 200;
        return maxDelay;
    }


});
