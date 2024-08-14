// Function to update (on /my-books page) the current page input to the total page number if the user updates teh status of their book to completed
function handleFormSubmit(bookId, totalPages) {
    const statusDropdown = document.getElementById('status_' + bookId);
    const currentPageInput = document.getElementById('current_page_' + bookId);
    
    if (statusDropdown.value === 'completed') {
        currentPageInput.value = totalPages;
    }
    
    return true;
}

// Function to confirm deletion of a book entry
function confirmDelete() {
    return confirm("Are you sure you want to delete this book from your list?");
}