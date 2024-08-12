// Function to update (on /my-books page) the current page input to the total page number if the user updates teh status of their book to completed
function handleFormSubmit(bookId, totalPages) {
    const statusDropdown = document.getElementById('status_' + bookId);
    const currentPageInput = document.getElementById('current_page_' + bookId);
    
    if (statusDropdown.value === 'completed') {
        currentPageInput.value = totalPages;
    }
    
    // Allow the form to be submitted
    return true;
}
