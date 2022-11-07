
set speechobject = createobject("sapi.spvoice")
set speechobject.Voice = speechobject.GetVoices.Item(1)
speechobject.rate = 0
speechobject.speak "i cant understand"
        
