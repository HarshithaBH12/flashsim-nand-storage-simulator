from flashsim import NANDFlash, FlashTranslationLayer

def test_write_and_read():
    flash = NANDFlash(2, 4)
    ftl = FlashTranslationLayer(flash)
    ftl.write(10, "hello")
    assert ftl.read(10) == "hello"

def test_update_invalidates_old_page():
    flash = NANDFlash(2, 4)
    ftl = FlashTranslationLayer(flash)
    ftl.write(1, "first")
    ftl.write(1, "second")
    assert ftl.read(1) == "second"
    assert flash.invalid_page_count() == 1
