//Interface alvo
interface MediaPlayer {
    void play(String audioType, String fileName);
}

//Classe que só toca MP3
class AudioPlayer implements MediaPlayer {
    public void play(String audioType, String fileName) {
        if (audioType.equalsIgnoreCase("mp3")) {
            System.out.println("Tocando mp3: " + fileName);
        } else {
            System.out.println("Formato nao suportado: " + audioType);
        }
    }
}

//Interface adaptada
interface AdvancedMediaPlayer {
    void playVlc(String fileName);
    void playMp4(String fileName);
}

//Implementação do AdvancedMediaPlayer para VLC
class VlcPlayer implements AdvancedMediaPlayer {
    public void playVlc(String fileName) {
        System.out.println("Tocando VLC: " + fileName);
    }

    public void playMp4(String fileName) {}
}

//Implementação do AdvancedMediaPlayer para MP4
class Mp4Player implements AdvancedMediaPlayer {
    public void playVlc(String fileName) {}

    public void playMp4(String fileName) {
        System.out.println("Tocando MP4: " + fileName);
    }
}

//Adapter que permite que o AudioPlayer toque VLC e MP4
class MediaAdapter implements MediaPlayer {
    AdvancedMediaPlayer advancedMediaPlayer;

    public MediaAdapter(String audioType) {
        if (audioType.equalsIgnoreCase("vlc")) {
            advancedMediaPlayer = new VlcPlayer();
        } else if (audioType.equalsIgnoreCase("mp4")) {
            advancedMediaPlayer = new Mp4Player();
        }
    }

    public void play(String audioType, String fileName) {
        if (audioType.equalsIgnoreCase("vlc")) {
            advancedMediaPlayer.playVlc(fileName);
        } else if (audioType.equalsIgnoreCase("mp4")) {
            advancedMediaPlayer.playMp4(fileName);
        }
    }
}

//Classe que usa o Adapter para tocar diferentes formatos
class AudioPlayerAdapterDemo {
    public static void main(String[] args) {
        MediaPlayer audioPlayer = new AudioPlayer();
        
        audioPlayer.play("mp3", "song.mp3");
        audioPlayer.play("mp4", "video.mp4"); //Não é suportado pelo AudioPlayer original

        MediaPlayer mediaAdapter = new MediaAdapter("mp4");
        mediaAdapter.play("mp4", "video.mp4"); //Agora é suportado pelo Adapter
    }
}
