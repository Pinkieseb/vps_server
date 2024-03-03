document.addEventListener('DOMContentLoaded', function() {
    const weightInput = document.getElementById('weight');
    const glucoseLevelInput = document.getElementById('glucoseLevel');
    const carbsInput = document.getElementById('totalCarbs');
    // Correctly target the span elements for dynamic updates
    const isfResult = document.getElementById('isfResult');
    const crResult = document.getElementById('crResult');
    const totalInsulinResult = document.getElementById('totalInsulinResult'); // Ensure this targets the p element directly

    [weightInput, glucoseLevelInput, carbsInput].forEach(input => input.addEventListener('input', updateCalculations));

    const detailsToggle = document.getElementById('detailsToggle');
    const details = document.getElementById('details');

    detailsToggle.addEventListener('click', function() {
        details.style.display = details.style.display === 'none' ? 'block' : 'none';
        detailsToggle.textContent = details.style.display === 'block' ? 'Hide' : 'More';
    });

    function updateCalculations() {
        const weight = parseFloat(weightInput.value) || 0;
        const glucoseLevel = parseFloat(glucoseLevelInput.value) || 0;
        const carbs = parseInt(carbsInput.value, 10) || 0;
        const { isf, cr } = calculateIsfAndCr(weight);

        isfResult.textContent = `${isf.mmol.toFixed(2)} mmol/L`;
        crResult.textContent = `1 unit covers ${cr.toFixed(2)} grams of carbs`;

        const insulinForCarbs = carbs / cr;
        const correctionDoseMin = calculateCorrectionDose(glucoseLevel, isf.mmol, 8); // Min insulin for 8 mmol/L target
        const correctionDoseMax = calculateCorrectionDose(glucoseLevel, isf.mmol, 2); // Max insulin for 2 mmol/L target

        const totalInsulinMin = insulinForCarbs + correctionDoseMin;
        const totalInsulinMax = insulinForCarbs + correctionDoseMax;

        totalInsulinResult.textContent = `Total Insulin Required: ${totalInsulinMin.toFixed(2)} to ${totalInsulinMax.toFixed(2)} units`;
    }

    function calculateIsfAndCr(weight) {
        const baseIsf = 1800 / weight; // mmol/L
        const baseCr = 500 / weight; // g/unit
        return { isf: { mmol: baseIsf }, cr: baseCr };
    }

    function calculateCorrectionDose(glucoseLevel, isf, targetGlucoseLevel) {
        if (glucoseLevel === 0 || isf === 0) {
            return 0;
        }
        return (glucoseLevel - targetGlucoseLevel) / isf;
    }
});