from flashsim import NANDFlash

def test_flash_initial_state():
    flash = NANDFlash(2, 4)
    assert flash.total_pages == 8
    assert flash.free_page_count() == 8
    assert flash.valid_page_count() == 0
