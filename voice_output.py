"""
Voice Output Module - Text-to-Speech for AI Agent
Uses macOS native 'say' command for zero-dependency TTS
"""

import subprocess
import threading
import platform
from config import ENABLE_VOICE, VOICE_NAME, VOICE_RATE

class VoiceOutput:
    """Text-to-speech output using macOS native say command."""
    
    def __init__(self):
        self.enabled = ENABLE_VOICE
        self.voice = VOICE_NAME
        self.rate = VOICE_RATE
        self.is_mac = platform.system() == 'Darwin'
        self._current_process = None
    
    def speak(self, text, async_mode=True):
        """
        Speak the given text.
        
        Args:
            text: Text to speak
            async_mode: If True, speaks in background thread (non-blocking)
        """
        if not self.enabled:
            return
        
        if not text or not text.strip():
            return
        
        # Clean text for speech
        clean_text = self._clean_text(text)
        
        if async_mode:
            thread = threading.Thread(target=self._speak_sync, args=(clean_text,))
            thread.daemon = True
            thread.start()
        else:
            self._speak_sync(clean_text)
    
    def _speak_sync(self, text):
        """Synchronous speech using system TTS."""
        try:
            if self.is_mac:
                # Use macOS 'say' command
                cmd = ['say', '-v', self.voice, '-r', str(self.rate), text]
                self._current_process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                self._current_process.wait()
            else:
                # Fallback for other platforms using pyttsx3 if available
                try:
                    import pyttsx3
                    engine = pyttsx3.init()
                    engine.setProperty('rate', self.rate)
                    engine.say(text)
                    engine.runAndWait()
                except ImportError:
                    print(f"[Voice] Would say: {text}")
        except Exception as e:
            print(f"[Voice] Error: {e}")
    
    def _clean_text(self, text):
        """Clean text for better speech output."""
        # Remove emojis and special characters that don't speak well
        replacements = {
            '✅': 'done',
            '❌': 'failed',
            '🎯': '',
            '📋': '',
            '🔍': '',
            '💭': '',
            '⏳': '',
            '🚀': '',
            '⚠️': 'warning',
            '🛑': 'stopped',
            '🤖': '',
            '💬': '',
            '📍': '',
            '⌨️': '',
            '🔘': '',
            '🔎': '',
            '🎵': '',
            '🌐': '',
            '📸': '',
            '🔄': '',
        }
        
        for emoji, replacement in replacements.items():
            text = text.replace(emoji, replacement)
        
        # Remove multiple spaces
        text = ' '.join(text.split())
        
        return text
    
    def stop(self):
        """Stop current speech."""
        if self._current_process:
            try:
                self._current_process.terminate()
            except:
                pass
    
    def set_enabled(self, enabled):
        """Enable or disable voice output."""
        self.enabled = enabled
    
    def set_voice(self, voice_name):
        """Change the voice."""
        self.voice = voice_name
    
    def set_rate(self, rate):
        """Change speech rate (words per minute)."""
        self.rate = rate


# Global instance
_voice = None

def get_voice():
    """Get or create the global voice output instance."""
    global _voice
    if _voice is None:
        _voice = VoiceOutput()
    return _voice

def speak(text, async_mode=True):
    """
    Convenience function to speak text.
    
    Args:
        text: Text to speak
        async_mode: If True, non-blocking (default)
    """
    get_voice().speak(text, async_mode)

def stop_speaking():
    """Stop current speech."""
    get_voice().stop()


# Quick test
if __name__ == "__main__":
    print("Testing voice output...")
    speak("Hello! I am your AI assistant. Ready to help you control your computer.", async_mode=False)
    print("Voice test complete.")
