function togglePhone(id) {
    const phoneEl = document.getElementById('phone-' + id);
    phoneEl.style.display = phoneEl.style.display === 'none' ? 'block' : 'none';
}
