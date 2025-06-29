document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form')
    const exportButton = document.getElementById('export-button')
    const startDateInput = document.getElementById('start_date')
    const endDateInput = document.getElementById('end_date')

    if (!endDateInput.value) {
        const today = new Date()
        endDateInput.value = today.toISOString().split('T')[0]
    }
    if (!startDateInput.value) {
        startDateInput.value = '2020-01-01'
    }

    exportButton.addEventListener('click', function() {
        const exportInput = document.createElement('input')
        exportInput.type = 'hidden'
        exportInput.name = 'export'
        exportInput.value = '1'

        form.appendChild(exportInput)
        form.submit()
        form.removeChild(exportInput)
    })
}
)