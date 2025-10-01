<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CrateJuice Sonic Postcards</title>
    <style>
        body {
            background: #1a1a1a;
            color: #fff;
            font-family: 'Courier New', monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            text-align: center;
        }

        .turntable {
            background: #333;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
        }

        .platter {
            width: 300px;
            height: 300px;
            background: radial-gradient(circle, #000 40%, #555);
            border-radius: 50%;
            margin: 0 auto;
            position: relative;
        }

        .platter.spinning {
            animation: spin 2s linear infinite;
        }

        @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .tonearm {
            width: 100px;
            height: 10px;
            background: #ccc;
            position: absolute;
            top: 50px;
            right: 50px;
            transform-origin: right;
        }

        .tonearm.playing {
            transform: rotate(-20deg);
        }

        .vu-meters {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
        }

        .vu-meter {
            width: 20px;
            height: 100px;
            background: linear-gradient(to top, #00ff00 0%, #333 0%);
            border: 1px solid #555;
        }

        .leds {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 10px;
        }

        .led {
            width: 10px;
            height: 10px;
            background: #333;
            border-radius: 50%;
        }

        .led.active { background: #00ff00; }
        .led.warning { background: #ff8800; }
        .led.danger { background: #ff0000; }

        .controls {
            margin-top: 20px;
        }

        button {
            background: #444;
            color: #fff;
            border: none;
            padding: 10px 20px;
            margin: 0 5px;
            cursor: pointer;
            font-family: 'Courier New', monospace;
        }

        button:hover {
            background: #666;
        }

        .playlist-container {
            margin-top: 20px;
            max-width: 600px;
            text-align: left;
        }

        .playlist-item {
            background: #222;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            cursor: pointer;
        }

        .playlist-item h3 {
            margin: 0 0 10px;
            color: #ff8800;
        }

        .playlist-item.solar-theme {
            background: linear-gradient(135deg, #ffcc00, #ff5500);
            box-shadow: 0 0 10px rgba(255, 204, 0, 0.5);
        }

        .playlist-item.solar-theme h3 {
            color: #fff;
        }

        .playlist-item.fortify-theme {
            background: linear-gradient(135deg, #555, #222);
            box-shadow: 0 0 10px rgba(255, 0, 0, 0.3);
        }

        .playlist-item.fortify-theme h3 {
            color: #ff3333;
        }

        .playlist-item ul {
            list-style: none;
            padding: 0;
        }

        .playlist-item li {
            padding: 5px 0;
            color: #ccc;
        }

        .playlist-item li:hover {
            color: #fff;
            background: #333;
        }

        .toast {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #444;
            color: #fff;
            padding: 10px 20px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="turntable">
            <div id="platter" class="platter"></div>
            <div id="tonearm" class="tonearm"></div>
            <div id="vinyl-content" class="vinyl-content"></div>
            <div class="controls">
                <button id="play-pause-btn">▶</button>
                <button id="next-btn">⏭</button>
                <button id="prev-btn">⏮</button>
                <button id="switch-view-btn">[playlists]</button>
            </div>
            <div class="vu-meters">
                <div id="vu-left-1" class="vu-meter"></div>
                <div id="vu-right-1" class="vu-meter"></div>
                <div id="vu-left-2" class="vu-meter"></div>
                <div id="vu-right-2" class="vu-meter"></div>
            </div>
            <div class="leds">
                <div id="ch1-led" class="led"></div>
                <div id="ch2-led" class="led"></div>
            </div>
        </div>
        <div id="playlist-container" class="playlist-container"></div>
        <iframe id="music-player" style="display: none;"></iframe>
    </div>
    <script>
        // Postcards for Sonic Postcards
        const postcards = [
            { id: 1, frontTitle: "TAPE<br>DECK", backHeader: "ANALOG SESSIONS", track: 'https://www.youtube.com/embed/Q22MCFC0CP0', note: 'Found this buried in the B-side collection. That warm analog saturation hits different when the lights are low. Turn it up and let it ride. - J' },
            { id: 9, frontTitle: "SPOTIFY<br>STREAM", backHeader: "PLAYLIST SPECIAL", track: 'https://open.spotify.com/embed/track/4iV5W9uYEdYUVa79Axb7Rh', trackType: 'spotify', note: 'Fresh from the underground playlist. This track captures that raw energy we chase in the crates. Stream it, feel it, live it. - Juice' }
        ];

        // Playlists including Rap Caviar, Solar Vibes, and Fortify Beats
        const playlists = [
            {
                id: 1,
                name: "Rap Caviar (Apple Music)",
                tracks: [
                    { id: 101, title: "Drake - No Face", url: 'https://www.youtube.com/embed/Q22MCFC0CP0', artist: "Drake" },
                    { id: 102, title: "Travis Scott - Sicko Mode", url: 'https://www.youtube.com/embed/ISV--pePI7M', artist: "Travis Scott" },
                    { id: 103, title: "Kendrick Lamar - Not Like Us", url: 'https://www.youtube.com/embed/_jgpVF9uZjQ', artist: "Kendrick Lamar" },
                    { id: 104, title: "Metro Boomin - Like That", url: 'https://www.youtube.com/embed/fM2YkUnaKR8', artist: "Metro Boomin" },
                    { id: 105, title: "21 Savage - Glock in My Lap", url: 'https://www.youtube.com/embed/tCnBrrnOefs', artist: "21 Savage" },
                    { id: 106, title: "Megan Thee Stallion - Mamushi", url: 'https://www.youtube.com/embed/CZe9YxJNs48', artist: "Megan Thee Stallion" },
                    { id: 107, title: "Future - Too Fast", url: 'https://www.youtube.com/embed/qcZ7e9EOQTY', artist: "Future" },
                    { id: 108, title: "Lil Baby - Sum 2 Prove", url: 'https://www.youtube.com/embed/pa14VNsdSYM', artist: "Lil Baby" },
                    { id: 109, title: "J. Cole - m y . l i f e", url: 'https://open.spotify.com/embed/track/4iV5W9uYEdYUVa79Axb7Rh', artist: "J. Cole" },
                    { id: 110, title: "Doja Cat - Paint The Town Red", url: 'https://www.youtube.com/embed/Q22MCFC0CP0', artist: "Doja Cat" }
                ]
            },
            {
                id: 2,
                name: "Solar Vibes",
                tracks: [
                    { id: 201, title: "The Weeknd - Blinding Lights", url: 'https://www.youtube.com/embed/ISV--pePI7M', artist: "The Weeknd" },
                    { id: 202, title: "SZA - Solar Power", url: 'https://www.youtube.com/embed/_jgpVF9uZjQ', artist: "SZA" },
                    { id: 203, title: "Flume - Sunlit", url: 'https://www.youtube.com/embed/fM2YkUnaKR8', artist: "Flume" },
                    { id: 204, title: "Tame Impala - Breathe Deeper", url: 'https://www.youtube.com/embed/tCnBrrnOefs', artist: "Tame Impala" },
                    { id: 205, title: "Anderson .Paak - Glowed Up", url: 'https://www.youtube.com/embed/CZe9YxJNs48', artist: "Anderson .Paak" }
                ]
            },
            {
                id: 3,
                name: "Fortify Beats",
                tracks: [
                    { id: 301, title: "Kendrick Lamar - King Kunta", url: 'https://www.youtube.com/embed/qcZ7e9EOQTY', artist: "Kendrick Lamar" },
                    { id: 302, title: "Pusha T - Numbers on the Boards", url: 'https://www.youtube.com/embed/pa14VNsdSYM', artist: "Pusha T" },
                    { id: 303, title: "Metro Boomin - Space Cadet", url: 'https://open.spotify.com/embed/track/4iV5W9uYEdYUVa79Axb7Rh', artist: "Metro Boomin" },
                    { id: 304, title: "21 Savage - Bank Account", url: 'https://www.youtube.com/embed/Q22MCFC0CP0', artist: "21 Savage" },
                    { id: 305, title: "JID - Surround Sound", url: 'https://www.youtube.com/embed/ISV--pePI7M', artist: "JID" }
                ]
            },
            { id: 4, name: "Underground Vibes", tracks: [1, 3, 5] },
            { id: 5, name: "Late Night Crates", tracks: [2, 4, 6] },
            { id: 6, name: "Street Corner Jams", tracks: [7, 8, 9] }
        ];

        // State management
        let currentIndex = 0;
        let currentPostcard = postcards[0];
        let audioContext = null;
        let analyser = null;
        let isPlaying = false;
        const stemStates = { vocals: false, drums: false, bass: false, other: false };
        let currentView = 'home';

        // Initialize audio context for VU meters
        function initAudioContext() {
            try {
                if (!audioContext) {
                    audioContext = new (window.AudioContext || window.webkitAudioContext)();
                    analyser = audioContext.createAnalyser();
                    analyser.fftSize = 256;
                }
            } catch (e) {
                console.error('AudioContext init failed:', e);
                showToast('AUDIO INIT FAILED');
            }
        }

        // Toggle playback for local MP3s and embeds
        function togglePlayback() {
            try {
                isPlaying = !isPlaying;
                const playPauseBtn = document.getElementById('play-pause-btn');
                const platter = document.getElementById('platter');
                const tonearm = document.getElementById('tonearm');
                const musicPlayer = document.getElementById('music-player');

                if (isPlaying) {
                    playPauseBtn.textContent = '⏸';
                    platter.classList.add('spinning');
                    tonearm.classList.add('playing');
                    if (currentPostcard.trackType === 'audio') {
                        const audio = new Audio(currentPostcard.track);
                        audio.play().catch(e => console.log('Audio playback failed:', e));
                        const source = audioContext.createMediaElementSource(audio);
                        source.connect(analyser);
                        analyser.connect(audioContext.destination);
                    } else if (musicPlayer && musicPlayer.contentWindow) {
                        try {
                            musicPlayer.contentWindow.postMessage('{"event":"command","func":"playVideo","args":""}', '*');
                        } catch (e) {
                            console.log('YouTube/SoundCloud control not available');
                        }
                    }
                    hapticFeedback('medium');
                    showToast('NOW PLAYING');
                } else {
                    playPauseBtn.textContent = '▶';
                    platter.classList.remove('spinning');
                    tonearm.classList.remove('playing');
                    if (musicPlayer && musicPlayer.contentWindow && currentPostcard.trackType !== 'audio') {
                        try {
                            musicPlayer.contentWindow.postMessage('{"event":"command","func":"pauseVideo","args":""}', '*');
                        } catch (e) {
                            console.log('YouTube/SoundCloud control not available');
                        }
                    }
                    hapticFeedback('light');
                    showToast('PAUSED');
                }
                saveState();
            } catch (e) {
                console.error('Playback toggle failed:', e);
                showToast('PLAYBACK ERROR');
            }
        }

        // Update playlist view
        function updatePlaylistView() {
            const playlistContainer = document.getElementById('playlist-container');
            if (currentView === 'playlists') {
                playlistContainer.innerHTML = `
                    <div class="playlist-list">
                        ${playlists.map(playlist => `
                            <div class="playlist-item ${playlist.name === 'Solar Vibes' ? 'solar-theme' : playlist.name === 'Fortify Beats' ? 'fortify-theme' : ''}" data-playlist-id="${playlist.id}">
                                <h3>${playlist.name}</h3>
                                <ul>
                                    ${playlist.tracks.map(track => `
                                        <li data-track-id="${track.id}">${track.artist} - ${track.title}</li>
                                    `).join('')}
                                </ul>
                            </div>
                        `).join('')}
                    </div>
                `;
                document.querySelectorAll('.playlist-item').forEach(item => {
                    item.addEventListener('click', () => {
                        const playlistId = parseInt(item.dataset.playlistId);
                        const playlist = playlists.find(p => p.id === playlistId);
                        currentPostcard = { id: playlistId, track: playlist.tracks[0].url, trackType: 'audio', note: `Now spinning ${playlist.name} - street vibes only.` };
                        updateVinylContent();
                        showToast(`LOADED ${playlist.name}`);
                    });
                });
            } else {
                playlistContainer.innerHTML = '';
            }
        }

        // Update vinyl content
        function updateVinylContent() {
            const vinylContent = document.getElementById('vinyl-content');
            vinylContent.innerHTML = `
                <div class="vinyl-label">
                    <h2>${currentPostcard.frontTitle || 'CRATE<br>JUICE'}</h2>
                    <p>${currentPostcard.backHeader || 'SONIC POSTCARDS'}</p>
                    <p>${currentPostcard.note || 'Spin the crates, feel the vibes.'}</p>
                </div>
            `;
            const musicPlayer = document.getElementById('music-player');
            musicPlayer.src = currentPostcard.trackType === 'audio' ? '' : currentPostcard.track;
        }

        // VU meter logic
        function updateVUMeters() {
            try {
                if (!analyser) return;
                const dataArray = new Uint8Array(analyser.frequencyBinCount);
                analyser.getByteFrequencyData(dataArray);
                const stemLevels = {
                    vocals: Math.max(...dataArray.slice(0, dataArray.length / 4)) / 255,
                    drums: Math.max(...dataArray.slice(dataArray.length / 4, dataArray.length / 2)) / 255,
                    bass: Math.max(...dataArray.slice(dataArray.length / 2, 3 * dataArray.length / 4)) / 255,
                    other: Math.max(...dataArray.slice(3 * dataArray.length / 4)) / 255
                };
                updateVUBar('vu-left-1', stemStates.vocals ? stemLevels.vocals : 0);
                updateVUBar('vu-right-1', stemStates.drums ? stemLevels.drums : 0);
                updateVUBar('vu-left-2', stemStates.bass ? stemLevels.bass : 0);
                updateVUBar('vu-right-2', stemStates.other ? stemLevels.other : 0);
                updateLEDs(Math.max(...Object.values(stemLevels)));
                requestAnimationFrame(updateVUMeters);
            } catch (e) {
                console.error('VU meter update failed:', e);
            }
        }

        function updateVUBar(elementId, level) {
            const bar = document.getElementById(elementId);
            if (bar) {
                const fill = Math.min(100, level * 100);
                bar.style.background = `linear-gradient(to top, ${fill > 85 ? '#ff0000' : fill > 75 ? '#ff8800' : fill > 60 ? '#ffff00' : '#00ff00'} ${fill}%, #333 ${fill}%)`;
            }
        }

        function updateLEDs(level) {
            const ch1Led = document.getElementById('ch1-led');
            const ch2Led = document.getElementById('ch2-led');
            [ch1Led, ch2Led].forEach(led => {
                if (led) led.classList.remove('active', 'warning', 'danger');
            });
            if (level > 0.8) {
                if (ch1Led) ch1Led.classList.add('danger');
                if (ch2Led) ch2Led.classList.add('warning');
            } else if (level > 0.6) {
                if (ch1Led) ch1Led.classList.add('warning');
                if (ch2Led) ch2Led.classList.add('active');
            } else if (level > 0.2) {
                if (ch1Led) ch1Led.classList.add('active');
            }
        }

        // Haptic feedback and toast
        function hapticFeedback(intensity) {
            if (navigator.vibrate) {
                navigator.vibrate(intensity === 'medium' ? 50 : 20);
            }
        }

        function showToast(message) {
            const toast = document.createElement('div');
            toast.className = 'toast';
            toast.textContent = message;
            document.body.appendChild(toast);
            setTimeout(() => toast.remove(), 2000);
        }

        // Save state to prevent data loss
        function saveState() {
            localStorage.setItem('crateJuiceState', JSON.stringify({
                currentIndex,
                currentView,
                stemStates,
                isPlaying
            }));
        }

        // Load state on init
        function loadState() {
            const state = JSON.parse(localStorage.getItem('crateJuiceState') || '{}');
            currentIndex = state.currentIndex || 0;
            currentView = state.currentView || 'home';
            Object.assign(stemStates, state.stemStates || {});
            isPlaying = state.isPlaying || false;
            if (isPlaying) togglePlayback();
        }

        // Placeholder for EQ, pitch, and crossfader (to be expanded)
        function initEQKnobs() { console.log('EQ knobs initialized'); }
        function initPitchControl() { console.log('Pitch control initialized'); }
        function initCrossfader() { console.log('Crossfader initialized'); }
        function initStemControls() { console.log('Stem controls initialized'); }

        // Initialize
        function init() {
            initAudioContext();
            updateVinylContent();
            updatePlaylistView();
            initEQKnobs();
            initPitchControl();
            initCrossfader();
            initStemControls();
            loadState();
            document.getElementById('play-pause-btn').addEventListener('click', togglePlayback);
            document.getElementById('next-btn').addEventListener('click', () => {
                currentIndex = (currentIndex + 1) % postcards.length;
                currentPostcard = postcards[currentIndex];
                updateVinylContent();
                showToast('NEXT TRACK');
            });
            document.getElementById('prev-btn').addEventListener('click', () => {
                currentIndex = (currentIndex - 1 + postcards.length) % postcards.length;
                currentPostcard = postcards[currentIndex];
                updateVinylContent();
                showToast('PREV TRACK');
            });
            document.getElementById('switch-view-btn').addEventListener('click', () => {
                currentView = currentView === 'home' ? 'playlists' : 'home';
                updatePlaylistView();
                showToast(currentView === 'playlists' ? 'PLAYLISTS LOADED' : 'HOME VIEW');
            });
        }

        init();
    </script>
</body>
</html>