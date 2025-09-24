<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>CrateJuice Sonic Postcards</title>
    
    <!-- PWA Meta Tags -->
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="CrateJuice">
    <meta name="theme-color" content="#8B4513">
    <meta name="mobile-web-app-capable" content="yes">
    
    <!-- Icons -->
    <link rel="apple-touch-icon" sizes="180x180" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 180 180'><rect width='180' height='180' fill='%23de7e2f'/><filter id='grit'><feTurbulence type='fractalNoise' baseFrequency='0.5' numOctaves='3' result='noise'/><feDisplacementMap in='SourceGraphic' in2='noise' scale='5' xChannelSelector='R' yChannelSelector='G'/></filter><rect width='180' height='180' fill='%23de7e2f' opacity='0.2' filter='url(%23grit)'/><text x='90' y='120' font-family='Courier Prime, monospace' font-size='120' font-weight='bold' fill='%23ffffff' text-anchor='middle' stroke='%23de7e2f' stroke-width='3' style='paint-order: stroke; letter-spacing: -5px;'>CJ</text><g opacity='0.3'><line x1='20' y1='30' x2='160' y2='30' stroke='%23000000' stroke-width='1' stroke-dasharray='5,5'/><line x1='30' y1='150' x2='150' y2='150' stroke='%23000000' stroke-width='1' stroke-dasharray='3,3'/><circle cx='90' cy='90' r='70' fill='none' stroke='%23000000' stroke-width='1' stroke-dasharray='10,5'/><path d='M40 60 Q90 100 140 60' fill='none' stroke='%23000000' stroke-width='2' stroke-dasharray='4,4'/></g><rect width='180' height='180' fill='none' stroke='%238b4513' stroke-width='8' rx='10'/></svg>">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' fill='%23de7e2f'/><filter id='grit'><feTurbulence type='fractalNoise' baseFrequency='0.5' numOctaves='3' result='noise'/><feDisplacementMap in='SourceGraphic' in2='noise' scale='5' xChannelSelector='R' yChannelSelector='G'/></filter><rect width='32' height='32' fill='%23de7e2f' opacity='0.2' filter='url(%23grit)'/><text x='16' y='22' font-family='Courier Prime, monospace' font-size='20' font-weight='bold' fill='%23ffffff' text-anchor='middle' stroke='%23de7e2f' stroke-width='0.5' style='paint-order: stroke; letter-spacing: -1px;'>CJ</text><g opacity='0.3'><line x1='4' y1='6' x2='28' y2='6' stroke='%23000000' stroke-width='0.2' stroke-dasharray='1,1'/><line x1='6' y1='26' x2='26' y2='26' stroke='%23000000' stroke-width='0.2' stroke-dasharray='0.6,0.6'/><circle cx='16' cy='16' r='11' fill='none' stroke='%23000000' stroke-width='0.2' stroke-dasharray='2,1'/><path d='M7 11 Q16 16 25 11' fill='none' stroke='%23000000' stroke-width='0.4' stroke-dasharray='0.8,0.8'/></g><rect width='32' height='32' fill='none' stroke='%238b4513' stroke-width='1.6' rx='2'/></svg>">
    
    <!-- Manifest -->
    <link rel="manifest" href="data:application/json,{
        'name': 'CrateJuice Sonic Postcards',
        'short_name': 'CrateJuice',
        'description': 'Sonic postcards from the underground',
        'start_url': '/',
        'display': 'standalone',
        'background_color': '#2d1810',
        'theme_color': '#8B4513',
        'orientation': 'portrait',
        'icons': [
            {
                'src': 'data:image/svg+xml,<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 192 192\"><rect width=\"192\" height=\"192\" fill=\"%23de7e2f\"/><filter id=\"grit\"><feTurbulence type=\"fractalNoise\" baseFrequency=\"0.5\" numOctaves=\"3\" result=\"noise\"/><feDisplacementMap in=\"SourceGraphic\" in2=\"noise\" scale=\"5\" xChannelSelector=\"R\" yChannelSelector=\"G\"/></filter><rect width=\"192\" height=\"192\" fill=\"%23de7e2f\" opacity=\"0.2\" filter=\"url(%23grit)\"/><text x=\"96\" y=\"128\" font-family=\"Courier Prime, monospace\" font-size=\"128\" font-weight=\"bold\" fill=\"%23ffffff\" text-anchor=\"middle\" stroke=\"%23de7e2f\" stroke-width=\"3\" style=\"paint-order: stroke; letter-spacing: -5px;\">CJ</text><g opacity=\"0.3\"><line x1=\"20\" y1=\"30\" x2=\"172\" y2=\"30\" stroke=\"%23000000\" stroke-width=\"1\" stroke-dasharray=\"5,5\"/><line x1=\"30\" y1=\"162\" x2=\"162\" y2=\"162\" stroke=\"%23000000\" stroke-width=\"1\" stroke-dasharray=\"3,3\"/><circle cx=\"96\" cy=\"96\" r=\"75\" fill=\"none\" stroke=\"%23000000\" stroke-width=\"1\" stroke-dasharray=\"10,5\"/><path d=\"M40 60 Q96 100 152 60\" fill=\"none\" stroke=\"%23000000\" stroke-width=\"2\" stroke-dasharray=\"4,4\"/></g><rect width=\"192\" height=\"192\" fill=\"none\" stroke=\"%238b4513\" stroke-width=\"8\" rx=\"10\"/></svg>',
                'sizes': '192x192',
                'type': 'image/svg+xml'
            },
            {
                'src': 'data:image/svg+xml,<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 512 512\"><rect width=\"512\" height=\"512\" fill=\"%23de7e2f\"/><filter id=\"grit\"><feTurbulence type=\"fractalNoise\" baseFrequency=\"0.5\" numOctaves=\"3\" result=\"noise\"/><feDisplacementMap in=\"SourceGraphic\" in2=\"noise\" scale=\"5\" xChannelSelector=\"R\" yChannelSelector=\"G\"/></filter><rect width=\"512\" height=\"512\" fill=\"%23de7e2f\" opacity=\"0.2\" filter=\"url(%23grit)\"/><text x=\"256\" y=\"350\" font-family=\"Courier Prime, monospace\" font-size=\"320\" font-weight=\"bold\" fill=\"%23ffffff\" text-anchor=\"middle\" stroke=\"%23de7e2f\" stroke-width=\"8\" style=\"paint-order: stroke; letter-spacing: -12px;\">CJ</text><g opacity=\"0.3\"><line x1=\"60\" y1=\"80\" x2=\"452\" y2=\"80\" stroke=\"%23000000\" stroke-width=\"2\" stroke-dasharray=\"10,10\"/><line x1=\"80\" y1=\"432\" x2=\"432\" y2=\"432\" stroke=\"%23000000\" stroke-width=\"2\" stroke-dasharray=\"6,6\"/><circle cx=\"256\" cy=\"256\" r=\"200\" fill=\"none\" stroke=\"%23000000\" stroke-width=\"2\" stroke-dasharray=\"20,10\"/><path d=\"M110 160 Q256 280 402 160\" fill=\"none\" stroke=\"%23000000\" stroke-width=\"4\" stroke-dasharray=\"8,8\"/></g><rect width=\"512\" height=\"512\" fill=\"none\" stroke=\"%238b4513\" stroke-width=\"16\" rx=\"20\"/></svg>',
                'sizes': '512x512',
                'type': 'image/svg+xml'
            }
        ]
    }">
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&display=swap');
        
        :root {
            --primary-orange: #de7e2f;
            --dark-brown: #8b4513;
            --cream: #f5e6d3;
            --dark-bg: #2d1810;
            --wood-brown: #8B4513;
            --metal-silver: #C0C0C0;
            --knob-black: #1a1a1a;
        }
        
        * { 
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
            -webkit-touch-callout: none;
            -webkit-user-select: none;
            user-select: none;
        }
        
        html, body {
            margin: 0;
            padding: 0;
            height: 100%;
            overflow-x: hidden;
            font-family: 'Courier Prime', monospace;
            background: linear-gradient(135deg, #8B4513 0%, #A0522D 50%, #8B4513 100%);
        }
        
        /* Mixing Board Background */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 20% 30%, rgba(160, 82, 45, 0.8) 0%, transparent 40%),
                radial-gradient(circle at 80% 70%, rgba(139, 69, 19, 0.6) 0%, transparent 40%),
                linear-gradient(45deg, transparent 49%, rgba(0,0,0,0.02) 50%, transparent 51%),
                repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.03) 2px, rgba(0,0,0,0.03) 4px);
            z-index: -1;
        }
        
        .app-container {
            min-height: 100vh;
            padding: env(safe-area-inset-top, 20px) 15px env(safe-area-inset-bottom, 20px) 15px;
            display: flex;
            flex-direction: column;
        }
        
        /* App Header with Patch Bay LED Title */
        .app-header {
            text-align: center;
            margin-bottom: 20px;
            padding: 25px;
            background: 
                radial-gradient(circle at 20% 30%, rgba(0,0,0,0.8) 2px, transparent 2px),
                radial-gradient(circle at 80% 70%, rgba(0,0,0,0.6) 1px, transparent 1px),
                radial-gradient(circle at 50% 50%, rgba(139, 69, 19, 0.3) 0%, transparent 60%),
                linear-gradient(135deg, #8B4513 0%, #654321 20%, #3E2723 40%, #2E1B13 60%, #1E0E0A 100%);
            border-radius: 12px;
            box-shadow: 
                0 12px 40px rgba(0,0,0,0.6),
                inset 0 3px 0 rgba(255,255,255,0.1),
                inset 0 -3px 0 rgba(0,0,0,0.5),
                inset -3px 0 8px rgba(0,0,0,0.4),
                inset 3px 0 8px rgba(0,0,0,0.3);
            border: 4px solid rgba(101, 67, 33, 0.8);
            position: relative;
            overflow: hidden;
        }
        
        .app-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                linear-gradient(45deg, transparent 0%, transparent 48%, rgba(0,0,0,0.1) 49%, rgba(0,0,0,0.1) 51%, transparent 52%),
                linear-gradient(-45deg, transparent 0%, transparent 48%, rgba(0,0,0,0.08) 49%, rgba(0,0,0,0.08) 51%, transparent 52%),
                repeating-linear-gradient(90deg, 
                    transparent 0px, 
                    transparent 3px, 
                    rgba(0,0,0,0.03) 3px, 
                    rgba(0,0,0,0.03) 6px
                ),
                repeating-linear-gradient(0deg, 
                    transparent 0px, 
                    transparent 3px, 
                    rgba(139, 69, 19, 0.02) 3px, 
                    rgba(139, 69, 19, 0.02) 6px
                );
            border-radius: 12px;
            pointer-events: none;
        }
        
        .app-header::after {
            content: '';
            position: absolute;
            top: 15px;
            left: 20px;
            width: 80%;
            height: 60%;
            background: 
                radial-gradient(circle at 25% 25%, rgba(0,0,0,0.6) 0%, transparent 30%),
                radial-gradient(circle at 75% 75%, rgba(139, 69, 19, 0.3) 0%, transparent 40%);
            border-radius: 8px;
            pointer-events: none;
        }
        
        .patch-bay-title {
            position: relative;
            z-index: 2;
            margin: 0;
            padding: 20px 0;
        }
        
        .led-word {
            display: inline-block;
            margin: 0 15px;
            position: relative;
        }
        
        .led-letter {
            display: inline-block;
            width: 40px;
            height: 40px;
            margin: 0 3px;
            position: relative;
            background: 
                radial-gradient(circle at 30% 30%, #2a2a2a 0%, #1a1a1a 50%, #0a0a0a 100%);
            border: 3px solid #333;
            border-radius: 50%;
            box-shadow: 
                0 4px 12px rgba(0,0,0,0.6),
                inset 0 2px 8px rgba(0,0,0,0.8),
                inset 0 -2px 4px rgba(255,255,255,0.1);
        }
        
        .led-letter::before {
            content: attr(data-letter);
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-family: 'Courier Prime', monospace;
            font-size: 18px;
            font-weight: 700;
            color: #ff4444;
            text-shadow: 
                0 0 8px #ff4444,
                0 0 16px rgba(255, 68, 68, 0.8),
                0 0 24px rgba(255, 68, 68, 0.6);
            animation: ledFlicker 3s infinite;
        }
        
        .led-letter::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 30px;
            height: 30px;
            background: 
                radial-gradient(circle, rgba(255, 68, 68, 0.3) 0%, transparent 70%);
            border-radius: 50%;
            animation: ledGlow 3s infinite;
        }
        
        /* Individual LED flickering patterns */
        .led-letter:nth-child(1)::before { animation-delay: 0s; }
        .led-letter:nth-child(2)::before { animation-delay: 0.2s; }
        .led-letter:nth-child(3)::before { animation-delay: 0.4s; }
        .led-letter:nth-child(4)::before { animation-delay: 0.6s; }
        .led-letter:nth-child(5)::before { animation-delay: 0.8s; }
        .led-letter:nth-child(6)::before { animation-delay: 1s; }
        .led-letter:nth-child(7)::before { animation-delay: 1.2s; }
        .led-letter:nth-child(8)::before { animation-delay: 1.4s; }
        .led-letter:nth-child(9)::before { animation-delay: 1.6s; }
        .led-letter:nth-child(10)::before { animation-delay: 1.8s; }
        
        .led-letter:nth-child(1)::after { animation-delay: 0s; }
        .led-letter:nth-child(2)::after { animation-delay: 0.2s; }
        .led-letter:nth-child(3)::after { animation-delay: 0.4s; }
        .led-letter:nth-child(4)::after { animation-delay: 0.6s; }
        .led-letter:nth-child(5)::after { animation-delay: 0.8s; }
        .led-letter:nth-child(6)::after { animation-delay: 1s; }
        .led-letter:nth-child(7)::after { animation-delay: 1.2s; }
        .led-letter:nth-child(8)::after { animation-delay: 1.4s; }
        .led-letter:nth-child(9)::after { animation-delay: 1.6s; }
        .led-letter:nth-child(10)::after { animation-delay: 1.8s; }
        
        @keyframes ledFlicker {
            0%, 90%, 100% { 
                opacity: 1; 
                color: #ff4444;
                text-shadow: 
                    0 0 8px #ff4444,
                    0 0 16px rgba(255, 68, 68, 0.8),
                    0 0 24px rgba(255, 68, 68, 0.6);
            }
            91%, 99% { 
                opacity: 0.3; 
                color: #663333;
                text-shadow: 
                    0 0 2px #663333,
                    0 0 4px rgba(102, 51, 51, 0.4);
            }
            95% { 
                opacity: 0.8; 
                color: #dd3333;
                text-shadow: 
                    0 0 6px #dd3333,
                    0 0 12px rgba(221, 51, 51, 0.6);
            }
        }
        
        @keyframes ledGlow {
            0%, 90%, 100% { 
                opacity: 0.6; 
                transform: translate(-50%, -50%) scale(1);
                background: radial-gradient(circle, rgba(255, 68, 68, 0.3) 0%, transparent 70%);
            }
            91%, 99% { 
                opacity: 0.1; 
                transform: translate(-50%, -50%) scale(0.8);
                background: radial-gradient(circle, rgba(102, 51, 51, 0.2) 0%, transparent 70%);
            }
            95% { 
                opacity: 0.4; 
                transform: translate(-50%, -50%) scale(0.9);
                background: radial-gradient(circle, rgba(221, 51, 51, 0.25) 0%, transparent 70%);
            }
        }
        
        .app-subtitle {
            color: var(--primary-orange);
            font-size: clamp(10px, 3vw, 14px);
            margin: 8px 0 0 0;
            letter-spacing: 2px;
            text-transform: uppercase;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
        }
        
        /* Mixing Board Panel */
        .mixing-panel {
            background: linear-gradient(135deg, #8B4513 0%, #A0522D 20%, #8B4513 100%);
            border-radius: 16px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 
                0 12px 40px rgba(0,0,0,0.4),
                inset 0 2px 0 rgba(255,255,255,0.1),
                inset 0 -2px 0 rgba(0,0,0,0.3);
            border: 2px solid rgba(139, 69, 19, 0.8);
        }
        
        .control-row {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        
        /* Knobs and Controls */
        /* Mixing Board Panel - Matching Patch Bay Texture */
        .mixing-panel {
            background: 
                radial-gradient(circle at 20% 30%, rgba(0,0,0,0.8) 2px, transparent 2px),
                radial-gradient(circle at 80% 70%, rgba(0,0,0,0.6) 1px, transparent 1px),
                radial-gradient(circle at 40% 60%, rgba(0,0,0,0.4) 1px, transparent 1px),
                radial-gradient(circle at 60% 20%, rgba(0,0,0,0.5) 2px, transparent 2px),
                radial-gradient(circle at 50% 50%, rgba(139, 69, 19, 0.3) 0%, transparent 60%),
                linear-gradient(135deg, #8B4513 0%, #654321 20%, #3E2723 40%, #2E1B13 60%, #1E0E0A 100%);
            border-radius: 16px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 
                0 12px 40px rgba(0,0,0,0.6),
                inset 0 3px 0 rgba(255,255,255,0.1),
                inset 0 -3px 0 rgba(0,0,0,0.5),
                inset -3px 0 8px rgba(0,0,0,0.4),
                inset 3px 0 8px rgba(0,0,0,0.3);
            border: 4px solid rgba(101, 67, 33, 0.8);
            position: relative;
            overflow: hidden;
        }
        
        .mixing-panel::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                linear-gradient(45deg, transparent 0%, transparent 48%, rgba(0,0,0,0.1) 49%, rgba(0,0,0,0.1) 51%, transparent 52%),
                linear-gradient(-45deg, transparent 0%, transparent 48%, rgba(0,0,0,0.08) 49%, rgba(0,0,0,0.08) 51%, transparent 52%),
                repeating-linear-gradient(90deg, 
                    transparent 0px, 
                    transparent 3px, 
                    rgba(0,0,0,0.03) 3px, 
                    rgba(0,0,0,0.03) 6px
                ),
                repeating-linear-gradient(0deg, 
                    transparent 0px, 
                    transparent 3px, 
                    rgba(139, 69, 19, 0.02) 3px, 
                    rgba(139, 69, 19, 0.02) 6px
                );
            border-radius: 16px;
            pointer-events: none;
        }
        
        .mixing-panel::after {
            content: '';
            position: absolute;
            top: 25px;
            right: 30px;
            width: 120px;
            height: 8px;
            background: linear-gradient(90deg, rgba(0,0,0,0.6) 0%, transparent 100%);
            border-radius: 4px;
            pointer-events: none;
        }
        
        /* Channel Strips - Matching Texture */
        .channel {
            background: 
                radial-gradient(circle at 80% 30%, rgba(0,0,0,0.6) 2px, transparent 2px),
                radial-gradient(circle at 20% 70%, rgba(0,0,0,0.4) 1px, transparent 1px),
                radial-gradient(circle at 60% 80%, rgba(0,0,0,0.3) 1px, transparent 1px),
                radial-gradient(circle at 50% 50%, rgba(139, 69, 19, 0.2) 0%, transparent 50%),
                linear-gradient(135deg, #654321 0%, #3E2723 30%, #2E1B13 60%, #1E0E0A 100%);
            border: 4px solid rgba(101, 67, 33, 0.8);
            border-radius: 12px;
            padding: 15px;
            min-width: 140px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 12px;
            position: relative;
            box-shadow: 
                inset 0 3px 6px rgba(0,0,0,0.6),
                inset 0 -2px 4px rgba(255,255,255,0.05),
                0 4px 12px rgba(0,0,0,0.4);
            overflow: hidden;
        }
        
        .channel::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                repeating-linear-gradient(90deg, 
                    transparent 0px, 
                    transparent 2px, 
                    rgba(0,0,0,0.02) 2px, 
                    rgba(0,0,0,0.02) 4px
                ),
                repeating-linear-gradient(45deg, 
                    transparent 0px, 
                    transparent 8px, 
                    rgba(139, 69, 19, 0.01) 8px, 
                    rgba(139, 69, 19, 0.01) 10px
                );
            border-radius: 12px;
            pointer-events: none;
        }
        
        .channel::after {
            content: '';
            position: absolute;
            bottom: 20px;
            right: 8px;
            width: 15px;
            height: 15px;
            background: radial-gradient(circle, rgba(0,0,0,0.3) 0%, transparent 70%);
            border-radius: 50%;
        }
        
        /* Turntable Section - Matching Texture */
        .turntable-section {
            background: 
                radial-gradient(circle at 25% 25%, rgba(0,0,0,0.7) 2px, transparent 2px),
                radial-gradient(circle at 75% 75%, rgba(0,0,0,0.5) 1px, transparent 1px),
                radial-gradient(circle at 30% 80%, rgba(0,0,0,0.4) 1px, transparent 1px),
                radial-gradient(circle at 70% 30%, rgba(0,0,0,0.6) 2px, transparent 2px),
                radial-gradient(circle at 50% 50%, rgba(139, 69, 19, 0.2) 0%, transparent 70%),
                linear-gradient(135deg, #654321 0%, #3E2723 25%, #2E1B13 50%, #1E0E0A 75%, #0A0502 100%);
            border: 4px solid rgba(101, 67, 33, 0.8);
            border-radius: 16px;
            padding: 25px;
            margin-top: 20px;
            position: relative;
            overflow: hidden;
            box-shadow: 
                0 8px 24px rgba(0,0,0,0.6),
                inset 0 3px 0 rgba(255,255,255,0.1),
                inset 0 -3px 0 rgba(0,0,0,0.5);
        }
        
        .turntable-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                linear-gradient(45deg, transparent 0%, transparent 47%, rgba(0,0,0,0.08) 48%, rgba(0,0,0,0.08) 52%, transparent 53%),
                linear-gradient(-45deg, transparent 0%, transparent 47%, rgba(0,0,0,0.06) 48%, rgba(0,0,0,0.06) 52%, transparent 53%),
                repeating-linear-gradient(90deg, 
                    transparent 0px, 
                    transparent 4px, 
                    rgba(0,0,0,0.02) 4px, 
                    rgba(0,0,0,0.02) 8px
                ),
                repeating-linear-gradient(0deg, 
                    transparent 0px, 
                    transparent 4px, 
                    rgba(139, 69, 19, 0.015) 4px, 
                    rgba(139, 69, 19, 0.015) 8px
                );
            border-radius: 16px;
            pointer-events: none;
        }
        
        .turntable-section::after {
            content: '';
            position: absolute;
            top: 20px;
            left: 25px;
            width: 60%;
            height: 40%;
            background: 
                radial-gradient(circle at 30% 30%, rgba(0,0,0,0.4) 0%, transparent 40%),
                radial-gradient(circle at 70% 70%, rgba(139, 69, 19, 0.2) 0%, transparent 50%);
            border-radius: 8px;
            pointer-events: none;
        }
        
        /* Vertical Pitch Control - Matching Texture */
        .pitch-control-vertical {
            background: 
                radial-gradient(circle at 30% 30%, rgba(0,0,0,0.6) 2px, transparent 2px),
                radial-gradient(circle at 70% 70%, rgba(0,0,0,0.4) 1px, transparent 1px),
                radial-gradient(circle at 50% 50%, rgba(139, 69, 19, 0.3) 0%, transparent 60%),
                linear-gradient(135deg, #654321 0%, #3E2723 30%, #2E1B13 60%, #1E0E0A 100%);
            border: 4px solid rgba(101, 67, 33, 0.9);
            box-shadow: 
                0 8px 20px rgba(0,0,0,0.7),
                inset 0 2px 4px rgba(255,255,255,0.1),
                inset 0 -2px 4px rgba(0,0,0,0.4);
            position: relative;
            overflow: hidden;
        }
        
        .pitch-control-vertical::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                repeating-linear-gradient(0deg, 
                    transparent 0px, 
                    transparent 3px, 
                    rgba(0,0,0,0.02) 3px, 
                    rgba(0,0,0,0.02) 6px
                ),
                repeating-linear-gradient(90deg, 
                    transparent 0px, 
                    transparent 2px, 
                    rgba(139, 69, 19, 0.015) 2px, 
                    rgba(139, 69, 19, 0.015) 4px
                );
            border-radius: 12px;
            pointer-events: none;
        }
        
        /* Channel Strips */
        .channel {
            background: 
                radial-gradient(circle at 80% 30%, rgba(0,0,0,0.3) 2px, transparent 2px),
                radial-gradient(circle at 20% 70%, rgba(0,0,0,0.2) 1px, transparent 1px),
                linear-gradient(135deg, rgba(101, 67, 33, 0.4) 0%, rgba(139, 69, 19, 0.3) 50%, rgba(93, 64, 55, 0.4) 100%);
            border: 3px solid rgba(101, 67, 33, 0.8);
            border-radius: 12px;
            padding: 15px;
            min-width: 140px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 12px;
            position: relative;
            box-shadow: 
                inset 0 2px 4px rgba(0,0,0,0.4),
                inset 0 -2px 4px rgba(255,255,255,0.05),
                0 2px 8px rgba(0,0,0,0.3);
        }
        
        .channel::before {
            content: '';
            position: absolute;
            top: 8px;
            left: 10px;
            width: 25px;
            height: 1px;
            background: rgba(0,0,0,0.4);
            transform: rotate(-15deg);
        }
        
        .channel::after {
            content: '';
            position: absolute;
            bottom: 20px;
            right: 8px;
            width: 15px;
            height: 15px;
            background: radial-gradient(circle, rgba(0,0,0,0.3) 0%, transparent 70%);
            border-radius: 50%;
        }
        
        /* Knobs with Wear */
        .eq-knob, .gain-knob, .knob {
            background: 
                radial-gradient(circle at 25% 25%, #F0F0F0 0%, #D0D0D0 30%, #A0A0A0 70%, #808080 100%);
            border: 3px solid #2a2a2a;
            position: relative;
            cursor: pointer;
            box-shadow: 
                0 4px 8px rgba(0,0,0,0.5),
                inset 0 2px 4px rgba(255,255,255,0.3),
                inset 0 -2px 4px rgba(0,0,0,0.2);
            transition: all 0.2s ease;
        }
        
        .eq-knob::after, .gain-knob::after, .knob::after {
            content: '';
            position: absolute;
            top: 20%;
            right: 15%;
            width: 30%;
            height: 30%;
            background: 
                radial-gradient(circle, rgba(0,0,0,0.2) 0%, transparent 60%),
                linear-gradient(45deg, rgba(0,0,0,0.1) 0%, transparent 50%);
            border-radius: 50%;
            pointer-events: none;
        }
        
        /* VU Meters - Backlit Analog Needle Style */
        .vu-meter {
            display: flex;
            gap: 8px;
            align-items: center;
            justify-content: center;
            height: 100px;
            margin-top: 15px;
            position: relative;
        }
        
        .vu-bar {
            width: 80px;
            height: 80px;
            background: 
                radial-gradient(circle at 50% 50%, #0a0a0a 0%, #000 100%);
            border: 4px solid #2a2a2a;
            border-radius: 50%;
            position: relative;
            overflow: visible;
            box-shadow: 
                0 4px 12px rgba(0,0,0,0.6),
                inset 0 2px 8px rgba(0,0,0,0.8),
                inset 0 -2px 4px rgba(255,255,255,0.1);
        }
        
        /* Backlit scale */
        .vu-bar::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 70px;
            height: 70px;
            transform: translate(-50%, -50%);
            background: 
                conic-gradient(from -90deg at 50% 50%,
                    rgba(0,255,0,0.3) 0deg,
                    rgba(102,255,0,0.3) 45deg,
                    rgba(204,255,0,0.3) 90deg,
                    rgba(255,204,0,0.3) 135deg,
                    rgba(255,102,0,0.3) 180deg,
                    rgba(255,0,0,0.3) 225deg,
                    rgba(255,0,0,0.3) 270deg
                );
            border-radius: 50%;
            opacity: 0.6;
            box-shadow: inset 0 0 20px rgba(0,255,0,0.2);
        }
        
        /* Needle */
        .vu-bar::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 2px;
            height: 30px;
            background: 
                linear-gradient(to top, 
                    rgba(255,255,255,0.9) 0%, 
                    rgba(255,68,68,0.9) 70%, 
                    rgba(255,255,255,1) 100%
                );
            transform-origin: bottom center;
            transform: translate(-50%, -100%) rotate(-60deg);
            border-radius: 1px;
            box-shadow: 
                0 0 8px rgba(255, 68, 68, 0.8),
                0 0 16px rgba(255, 68, 68, 0.4);
            transition: transform 0.1s ease-out;
            z-index: 10;
        }
        
        /* Scale markings with backlight */
        .vu-meter::before {
            content: '';
            position: absolute;
            width: 100px;
            height: 100px;
            background-image: 
                radial-gradient(1px circle at 20px 70px, rgba(0,255,0,0.6) 0%, transparent 2px),
                radial-gradient(1px circle at 35px 45px, rgba(204,255,0,0.6) 0%, transparent 2px),
                radial-gradient(1px circle at 50px 35px, rgba(255,204,0,0.6) 0%, transparent 2px),
                radial-gradient(1px circle at 65px 45px, rgba(255,102,0,0.6) 0%, transparent 2px),
                radial-gradient(1px circle at 80px 70px, rgba(255,0,0,0.6) 0%, transparent 2px);
            pointer-events: none;
            z-index: 1;
        }
        
        /* Center pivot point */
        .vu-meter::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 6px;
            height: 6px;
            background: 
                radial-gradient(circle, #ffffff 0%, #c0c0c0 50%, #808080 100%);
            border: 1px solid #333;
            border-radius: 50%;
            transform: translate(-50%, -50%);
            z-index: 15;
            box-shadow: 0 2px 4px rgba(0,0,0,0.4);
        }
        
        /* Chrome Heavy Duty Knobs */
        .eq-knob, .gain-knob {
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: 
                radial-gradient(circle at 30% 30%, #ffffff 0%, #e0e0e0 20%, #c0c0c0 40%, #a0a0a0 60%, #808080 80%, #606060 100%);
            border: 4px solid #2a2a2a;
            position: relative;
            cursor: pointer;
            box-shadow: 
                0 6px 12px rgba(0,0,0,0.6),
                inset 0 3px 6px rgba(255,255,255,0.4),
                inset 0 -3px 6px rgba(0,0,0,0.3);
            transition: all 0.2s ease;
        }
        
        .eq-knob::before, .gain-knob::before {
            content: '';
            position: absolute;
            top: 4px;
            left: 50%;
            transform: translateX(-50%);
            width: 4px;
            height: 18px;
            background: linear-gradient(to bottom, #1a1a1a 0%, #000 100%);
            border-radius: 2px;
            box-shadow: inset 0 1px 2px rgba(0,0,0,0.8);
        }
        
        .eq-knob::after, .gain-knob::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 8px;
            height: 8px;
            background: 
                radial-gradient(circle, #ffffff 0%, #c0c0c0 50%, #808080 100%);
            border: 1px solid #2a2a2a;
            border-radius: 50%;
        }
        
        /* Main Navigation Knobs - Even Bigger */
        .knob {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: 
                radial-gradient(circle at 25% 25%, #ffffff 0%, #f0f0f0 15%, #d0d0d0 30%, #b0b0b0 50%, #909090 70%, #707070 85%, #505050 100%);
            border: 5px solid #1a1a1a;
            position: relative;
            cursor: pointer;
            box-shadow: 
                0 8px 16px rgba(0,0,0,0.7),
                inset 0 4px 8px rgba(255,255,255,0.5),
                inset 0 -4px 8px rgba(0,0,0,0.4);
            transition: all 0.2s ease;
        }
        
        .knob::before {
            content: '';
            position: absolute;
            top: 6px;
            left: 50%;
            transform: translateX(-50%);
            width: 5px;
            height: 22px;
            background: linear-gradient(to bottom, #000 0%, #333 100%);
            border-radius: 2px;
            box-shadow: 
                inset 0 1px 2px rgba(0,0,0,0.8),
                0 1px 0 rgba(255,255,255,0.3);
        }
        
        /* Crossfader - Heavy Duty Chrome */
        .crossfader-slider {
            position: relative;
            width: 150px;
            height: 30px;
            background: 
                linear-gradient(to bottom, #2a2a2a 0%, #1a1a1a 50%, #0a0a0a 100%);
            border-radius: 15px;
            border: 4px solid #333;
            cursor: pointer;
            box-shadow: 
                0 4px 12px rgba(0,0,0,0.6),
                inset 0 4px 8px rgba(0,0,0,0.8);
        }
        
        .crossfader-thumb {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 35px;
            height: 24px;
            background: 
                linear-gradient(to bottom, #ffffff 0%, #e0e0e0 20%, #c0c0c0 50%, #a0a0a0 80%, #808080 100%);
            border: 3px solid #2a2a2a;
            border-radius: 6px;
            transition: all 0.2s ease;
            box-shadow: 
                0 4px 8px rgba(0,0,0,0.5),
                inset 0 2px 4px rgba(255,255,255,0.4);
        }
        
        .crossfader-thumb::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 20px;
            height: 2px;
            background: #333;
            border-radius: 1px;
        }
        
        .crossfader-thumb::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 2px;
            height: 12px;
            background: #333;
            border-radius: 1px;
        }
        
        /* Vertical Pitch Control - Right Side */
        .pitch-control-vertical {
            position: absolute;
            right: -80px;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 15px;
            background: 
                linear-gradient(135deg, rgba(139, 69, 19, 0.8) 0%, rgba(101, 67, 33, 0.9) 100%);
            padding: 20px 15px;
            border-radius: 12px;
            border: 3px solid #333;
            box-shadow: 
                0 8px 20px rgba(0,0,0,0.6),
                inset 0 2px 4px rgba(255,255,255,0.1);
        }
        
        .pitch-label-vertical {
            font-size: 10px;
            font-weight: 700;
            color: var(--cream);
            text-transform: uppercase;
            letter-spacing: 1px;
            writing-mode: vertical-rl;
            text-orientation: mixed;
        }
        
        .pitch-slider-vertical {
            position: relative;
            width: 25px;
            height: 150px;
            background: 
                linear-gradient(to bottom, #2a2a2a 0%, #1a1a1a 50%, #0a0a0a 100%);
            border-radius: 12px;
            border: 4px solid #333;
            cursor: pointer;
            box-shadow: 
                0 4px 12px rgba(0,0,0,0.6),
                inset 0 4px 8px rgba(0,0,0,0.8);
        }
        
        .pitch-track-vertical {
            position: absolute;
            top: 15px;
            bottom: 15px;
            left: 50%;
            transform: translateX(-50%);
            width: 2px;
            background: var(--primary-orange);
        }
        
        .pitch-thumb-vertical {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 30px;
            height: 20px;
            background: 
                linear-gradient(to bottom, #ffffff 0%, #e0e0e0 20%, #c0c0c0 50%, #a0a0a0 80%, #808080 100%);
            border: 3px solid #2a2a2a;
            border-radius: 4px;
            transition: all 0.2s ease;
            box-shadow: 
                0 4px 8px rgba(0,0,0,0.5),
                inset 0 2px 4px rgba(255,255,255,0.4);
            cursor: grab;
        }
        
        .pitch-thumb-vertical:active {
            cursor: grabbing;
            transform: translate(-50%, -50%) scale(0.95);
        }
        
        .pitch-thumb-vertical::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 16px;
            height: 2px;
            background: #333;
            border-radius: 1px;
        }
        
        .pitch-readout-vertical {
            font-size: 9px;
            font-weight: 700;
            color: var(--primary-orange);
            font-family: 'Courier New', monospace;
            background: 
                linear-gradient(135deg, #1a1a1a 0%, #0a0a0a 100%);
            padding: 4px 8px;
            border-radius: 4px;
            border: 2px solid #333;
            min-width: 50px;
            text-align: center;
            box-shadow: 
                inset 0 2px 4px rgba(0,0,0,0.8),
                0 2px 4px rgba(0,0,0,0.3);
        }
        
        /* Main Controls Container */
        .main-controls-container {
            position: relative;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        /* Vertical Pitch Control - Right Side */
        .pitch-control-vertical {
            position: absolute;
            right: -90px;
            top: 0;
            height: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 15px;
            background: 
                radial-gradient(circle at 30% 30%, rgba(0,0,0,0.4) 2px, transparent 2px),
                linear-gradient(135deg, rgba(139, 69, 19, 0.8) 0%, rgba(101, 67, 33, 0.9) 100%);
            padding: 25px 15px;
            border-radius: 12px;
            border: 3px solid #333;
            box-shadow: 
                0 8px 20px rgba(0,0,0,0.6),
                inset 0 2px 4px rgba(255,255,255,0.1),
                inset 0 -2px 4px rgba(0,0,0,0.3);
            width: 80px;
            z-index: 10;
        }
        
        /* Adjust mixing panel to show pitch control */
        .app-container {
            padding-right: 120px;
        }
        
        /* Turntable with Heavy Wear */
        .turntable-base {
            width: 280px;
            height: 280px;
            background: 
                radial-gradient(circle at 70% 30%, rgba(0,0,0,0.4) 2px, transparent 2px),
                radial-gradient(circle at 30% 70%, rgba(0,0,0,0.3) 1px, transparent 1px),
                radial-gradient(circle at 50% 50%, #1a1a1a 30%, #0a0a0a 70%, #000000 100%);
            border-radius: 50%;
            border: 8px solid #2a2a2a;
            position: relative;
            box-shadow: 
                0 20px 50px rgba(0,0,0,0.8),
                inset 0 8px 16px rgba(255,255,255,0.1),
                inset 0 -8px 16px rgba(0,0,0,0.5),
                inset 4px 4px 8px rgba(0,0,0,0.3);
        }
        
        .turntable-base::before {
            content: '';
            position: absolute;
            top: 20px;
            left: 40px;
            width: 80px;
            height: 2px;
            background: linear-gradient(90deg, rgba(0,0,0,0.6) 0%, transparent 100%);
            transform: rotate(25deg);
        }
        
        .turntable-base::after {
            content: '';
            position: absolute;
            bottom: 60px;
            right: 30px;
            width: 40px;
            height: 40px;
            background: radial-gradient(circle, rgba(0,0,0,0.4) 0%, transparent 70%);
            border-radius: 50%;
        }
        
        /* Technics 1210 Style Strobe Light */
        .strobe-light {
            position: absolute;
            top: -15px;
            right: 20px;
            width: 60px;
            height: 12px;
            background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
            border: 2px solid #333;
            border-radius: 6px;
            box-shadow: 
                0 4px 8px rgba(0,0,0,0.6),
                inset 0 1px 2px rgba(255,255,255,0.1);
            overflow: hidden;
        }
        
        .strobe-dots {
            position: absolute;
            top: 50%;
            left: 0;
            right: 0;
            transform: translateY(-50%);
            display: flex;
            justify-content: space-around;
            align-items: center;
            height: 100%;
        }
        
        .strobe-dot {
            width: 3px;
            height: 3px;
            background: #ff4444;
            border-radius: 50%;
            opacity: 0.3;
            box-shadow: 0 0 4px rgba(255, 68, 68, 0.8);
            animation: strobePulse 1s infinite;
        }
        
        .strobe-dot:nth-child(1) {
            animation: strobeRotate1 2s linear infinite;
        }
        
        .strobe-dot:nth-child(2) {
            animation: strobeRotate2 1.8s linear infinite reverse;
        }
        
        .strobe-dot:nth-child(3) {
            animation: strobeRotate3 2.2s linear infinite;
        }
        
        .strobe-dot:nth-child(4) {
            animation: strobeRotate4 1.9s linear infinite reverse;
        }
        
        @keyframes strobeRotate1 {
            0% { opacity: 1; transform: translateX(0px); }
            25% { opacity: 0.3; transform: translateX(8px); }
            50% { opacity: 1; transform: translateX(16px); }
            75% { opacity: 0.3; transform: translateX(24px); }
            100% { opacity: 1; transform: translateX(32px); }
        }
        
        @keyframes strobeRotate2 {
            0% { opacity: 0.8; transform: translateX(32px); }
            25% { opacity: 0.2; transform: translateX(24px); }
            50% { opacity: 0.8; transform: translateX(16px); }
            75% { opacity: 0.2; transform: translateX(8px); }
            100% { opacity: 0.8; transform: translateX(0px); }
        }
        
        @keyframes strobeRotate3 {
            0% { opacity: 0.6; transform: translateX(0px); }
            33% { opacity: 1; transform: translateX(12px); }
            66% { opacity: 0.3; transform: translateX(24px); }
            100% { opacity: 0.6; transform: translateX(36px); }
        }
        
        @keyframes strobeRotate4 {
            0% { opacity: 0.9; transform: translateX(36px); }
            33% { opacity: 0.4; transform: translateX(24px); }
            66% { opacity: 0.9; transform: translateX(12px); }
            100% { opacity: 0.9; transform: translateX(0px); }
        }
        
        .platter {
            width: 220px;
            height: 220px;
            background: 
                radial-gradient(circle at 30% 30%, rgba(255,255,255,0.1) 0%, transparent 20%),
                radial-gradient(circle at 70% 70%, rgba(0,0,0,0.3) 0%, transparent 30%),
                radial-gradient(circle, #1a1a1a 0%, #0a0a0a 60%, #000000 100%);
            border-radius: 50%;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            border: 4px solid #3a3a3a;
            transition: transform 0.5s ease;
            box-shadow: 
                inset 0 4px 8px rgba(0,0,0,0.5),
                inset 0 -2px 4px rgba(255,255,255,0.1);
        }
        
        .record-grooves {
            position: absolute;
            top: 10px;
            left: 10px;
            right: 10px;
            bottom: 10px;
            border-radius: 50%;
            background: 
                repeating-radial-gradient(
                    circle,
                    transparent 0px,
                    transparent 3px,
                    rgba(255,255,255,0.05) 3px,
                    rgba(255,255,255,0.05) 4px
                ),
                repeating-radial-gradient(
                    circle,
                    transparent 0px,
                    transparent 8px,
                    rgba(0,0,0,0.1) 8px,
                    rgba(0,0,0,0.1) 9px
                );
            pointer-events: none;
        }
        
        /* Tonearm with Battle Damage */
        .tonearm-arm {
            width: 100px;
            height: 4px;
            background: 
                linear-gradient(to right, #999 0%, #777 30%, #555 70%, #666 100%);
            border-radius: 2px;
            position: absolute;
            left: 10px;
            top: 50%;
            transform: translateY(-50%);
            box-shadow: 
                0 2px 4px rgba(0,0,0,0.4),
                inset 0 1px 0 rgba(255,255,255,0.2);
            position: relative;
        }
        
        .tonearm-arm::before {
            content: '';
            position: absolute;
            top: -1px;
            left: 60%;
            width: 15px;
            height: 1px;
            background: rgba(0,0,0,0.4);
        }
        
        /* Buttons with Heavy Use */
        .nav-button, .action-btn {
            background: 
                radial-gradient(circle at 30% 30%, rgba(255,255,255,0.1) 0%, transparent 40%),
                linear-gradient(135deg, var(--primary-orange) 0%, #C96D28 50%, #A0522D 100%);
            border: 3px solid var(--dark-brown);
            box-shadow: 
                0 6px 12px rgba(0,0,0,0.4),
                inset 0 2px 0 rgba(255,255,255,0.2),
                inset 0 -2px 0 rgba(0,0,0,0.3);
            position: relative;
        }
        
        .nav-button::before, .action-btn::before {
            content: '';
            position: absolute;
            top: 20%;
            right: 15%;
            width: 30%;
            height: 30%;
            background: radial-gradient(circle, rgba(0,0,0,0.15) 0%, transparent 60%);
            border-radius: 50%;
        }
        
        .play-pause-btn {
            background: 
                radial-gradient(circle at 25% 25%, rgba(255,255,255,0.2) 0%, transparent 50%),
                radial-gradient(circle at 75% 75%, rgba(0,0,0,0.3) 0%, transparent 50%),
                linear-gradient(135deg, var(--primary-orange) 0%, #C96D28 100%);
            border: 4px solid var(--dark-brown);
            box-shadow: 
                0 6px 16px rgba(0,0,0,0.5),
                inset 0 3px 0 rgba(255,255,255,0.3),
                inset 0 -3px 0 rgba(0,0,0,0.4);
        }
        
        /* Postcard with Aged Edges */
        .postcard-face {
            box-shadow: 
                0 25px 50px rgba(0,0,0,0.4),
                inset 0 0 0 6px var(--cream),
                inset 0 0 0 8px rgba(139, 69, 19, 0.3);
            position: relative;
        }
        
        .postcard-face::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 85% 15%, rgba(139, 69, 19, 0.2) 0%, transparent 20%),
                radial-gradient(circle at 15% 85%, rgba(139, 69, 19, 0.15) 0%, transparent 25%),
                linear-gradient(45deg, transparent 0%, rgba(139, 69, 19, 0.05) 50%, transparent 100%);
            border-radius: 12px;
            pointer-events: none;
        }
        
        .postcard-front {
            position: relative;
        }
        
        .postcard-front::after {
            content: '';
            position: absolute;
            top: 20px;
            right: 25px;
            width: 40px;
            height: 2px;
            background: rgba(0,0,0,0.2);
            transform: rotate(-5deg);
        }
        
        /* Channel Strips */
        .channel-strip {
            display: flex;
            justify-content: space-around;
            gap: 20px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }
        
        .channel {
            background: rgba(139, 69, 19, 0.3);
            border: 2px solid rgba(139, 69, 19, 0.6);
            border-radius: 12px;
            padding: 15px;
            min-width: 140px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 12px;
        }
        
        .channel-label {
            font-size: 11px;
            font-weight: 700;
            color: var(--cream);
            text-align: center;
            margin-bottom: 5px;
        }
        
        /* LED Indicators */
        .led-indicator {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #333;
            border: 2px solid #666;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.5);
            transition: all 0.3s ease;
        }
        
        .led-indicator.active {
            background: #00ff00;
            border-color: #00cc00;
            box-shadow: 
                inset 0 2px 4px rgba(0,0,0,0.3),
                0 0 12px #00ff00,
                0 0 24px rgba(0,255,0,0.3);
        }
        
        .led-indicator.warning {
            background: #ffaa00;
            border-color: #cc8800;
            box-shadow: 
                inset 0 2px 4px rgba(0,0,0,0.3),
                0 0 12px #ffaa00,
                0 0 24px rgba(255,170,0,0.3);
        }
        
        .led-indicator.danger {
            background: #ff0000;
            border-color: #cc0000;
            box-shadow: 
                inset 0 2px 4px rgba(0,0,0,0.3),
                0 0 12px #ff0000,
                0 0 24px rgba(255,0,0,0.3);
        }
        
        /* EQ Section */
        .eq-section {
            display: flex;
            flex-direction: column;
            gap: 10px;
            align-items: center;
        }
        
        .eq-knob-group {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 5px;
        }
        
        .eq-knob-group label {
            font-size: 8px;
            font-weight: 700;
            color: var(--cream);
            text-transform: uppercase;
        }
        
        .eq-knob {
            width: 35px;
            height: 35px;
            border-radius: 50%;
            background: radial-gradient(circle at 30% 30%, #E0E0E0, #A0A0A0);
            border: 2px solid var(--knob-black);
            position: relative;
            cursor: pointer;
            box-shadow: 
                0 3px 6px rgba(0,0,0,0.4),
                inset 0 1px 3px rgba(255,255,255,0.3);
            transition: all 0.2s ease;
        }
        
        .eq-knob::before {
            content: '';
            position: absolute;
            top: 3px;
            left: 50%;
            transform: translateX(-50%);
            width: 2px;
            height: 12px;
            background: var(--knob-black);
            border-radius: 1px;
        }
        
        /* Gain Knob */
        .gain-knob-group {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
        }
        
        .gain-knob-group label {
            font-size: 9px;
            font-weight: 700;
            color: var(--primary-orange);
            text-transform: uppercase;
        }
        
        .gain-knob {
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: radial-gradient(circle at 30% 30%, #E0E0E0, #A0A0A0);
            border: 3px solid var(--knob-black);
            position: relative;
            cursor: pointer;
            box-shadow: 
                0 4px 8px rgba(0,0,0,0.4),
                inset 0 2px 4px rgba(255,255,255,0.3);
            transition: all 0.2s ease;
        }
        
        .gain-knob::before {
            content: '';
            position: absolute;
            top: 4px;
            left: 50%;
            transform: translateX(-50%);
            width: 3px;
            height: 15px;
            background: var(--knob-black);
            border-radius: 2px;
        }
        
        /* VU Meters */
        .vu-meter {
            display: flex;
            gap: 3px;
            align-items: flex-end;
            height: 80px;
            margin-top: 10px;
        }
        
        .vu-bar {
            width: 8px;
            height: 100%;
            background: linear-gradient(
                to top,
                #00ff00 0%,
                #00ff00 60%,
                #ffff00 75%,
                #ff8800 85%,
                #ff0000 100%
            );
            border: 1px solid #333;
            border-radius: 2px;
            position: relative;
            overflow: hidden;
        }
        
        .vu-bar::before {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 30%;
            background: #333;
            transition: height 0.1s ease-out;
        }
        
        /* Crossfader */
        .crossfader-control {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
            margin: 0 20px;
        }
        
        .crossfader-label {
            font-size: 10px;
            font-weight: 700;
            color: var(--cream);
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .crossfader-slider {
            position: relative;
            width: 120px;
            height: 20px;
            background: var(--knob-black);
            border-radius: 10px;
            border: 2px solid var(--dark-brown);
            cursor: pointer;
        }
        
        .crossfader-track {
            position: absolute;
            top: 50%;
            left: 8px;
            right: 8px;
            transform: translateY(-50%);
            height: 2px;
            background: var(--primary-orange);
        }
        
        .crossfader-thumb {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 20px;
            height: 16px;
            background: radial-gradient(ellipse at center, #E0E0E0, #A0A0A0);
            border: 2px solid var(--knob-black);
            border-radius: 4px;
            transition: all 0.2s ease;
            box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        
        /* Stem Controls */
        .stem-controls {
            background: rgba(139, 69, 19, 0.2);
            border: 2px solid rgba(139, 69, 19, 0.4);
            border-radius: 12px;
            padding: 20px;
            margin-top: 20px;
        }
        
        .stem-section h4 {
            color: var(--cream);
            font-size: 12px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 15px;
            letter-spacing: 2px;
            text-transform: uppercase;
        }
        
        .stem-buttons {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
            margin-bottom: 15px;
        }
        
        .stem-btn {
            padding: 8px 12px;
            background: linear-gradient(135deg, #654321 0%, #8B4513 100%);
            color: var(--cream);
            border: 2px solid var(--dark-brown);
            border-radius: 6px;
            font-family: 'Courier Prime', monospace;
            font-weight: 700;
            font-size: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
        }
        
        .stem-btn:hover {
            background: linear-gradient(135deg, #8B4513 0%, #A0522D 100%);
        }
        
        .stem-btn.active {
            background: linear-gradient(135deg, var(--primary-orange) 0%, #C96D28 100%);
            box-shadow: 
                0 0 12px rgba(222, 126, 47, 0.5),
                inset 0 2px 4px rgba(255,255,255,0.2);
        }
        
        .stem-btn.processing {
            animation: processingPulse 1.5s infinite;
        }
        
        @keyframes processingPulse {
            0%, 100% { 
                box-shadow: 0 0 5px rgba(222, 126, 47, 0.3);
                transform: scale(1);
            }
            50% { 
                box-shadow: 0 0 20px rgba(222, 126, 47, 0.8);
                transform: scale(1.02);
            }
        }
        
        .download-btn {
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, var(--primary-orange) 0%, #C96D28 100%);
            color: var(--cream);
            border: 2px solid var(--dark-brown);
            border-radius: 8px;
            font-family: 'Courier Prime', monospace;
            font-weight: 700;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 2px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .download-btn:hover {
            background: linear-gradient(135deg, #C96D28 0%, var(--primary-orange) 100%);
            transform: translateY(-2px);
        }
        
        .download-btn:disabled {
            background: #666;
            color: #999;
            cursor: not-allowed;
            transform: none;
        }
        
        /* Turntable Section */
        .turntable-section {
            background: rgba(139, 69, 19, 0.2);
            border: 2px solid rgba(139, 69, 19, 0.4);
            border-radius: 16px;
            padding: 25px;
            margin-top: 20px;
        }
        
        .turntable-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .turntable-base {
            width: 280px;
            height: 280px;
            background: radial-gradient(circle, #2a2a2a 0%, #1a1a1a 100%);
            border-radius: 50%;
            border: 8px solid #333;
            position: relative;
            box-shadow: 
                0 15px 40px rgba(0,0,0,0.6),
                inset 0 8px 16px rgba(255,255,255,0.1),
                inset 0 -8px 16px rgba(0,0,0,0.3);
        }
        
        .platter {
            width: 220px;
            height: 220px;
            background: radial-gradient(circle, #1a1a1a 0%, #0a0a0a 100%);
            border-radius: 50%;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            border: 4px solid #444;
            transition: transform 0.5s ease;
        }
        
        .platter.spinning {
            animation: spin 2s linear infinite;
        }
        
        .platter.paused {
            animation-play-state: paused;
        }
        
        @keyframes spin {
            from { transform: translate(-50%, -50%) rotate(0deg); }
            to { transform: translate(-50%, -50%) rotate(360deg); }
        }
        
        .record-label {
            width: 140px;
            height: 140px;
            background: var(--primary-orange);
            border-radius: 50%;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            border: 3px solid var(--dark-brown);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .postcard-vinyl {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: var(--cream);
            border: 2px solid var(--dark-brown);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            position: relative;
        }
        
        .vinyl-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 15px;
        }
        
        .vinyl-content .cassette-icon {
            width: 40px;
            height: 28px;
            margin-bottom: 8px;
        }
        
        .vinyl-title {
            font-size: 9px;
            font-weight: 700;
            color: var(--dark-brown);
            text-transform: uppercase;
            letter-spacing: 1px;
            line-height: 1;
            text-shadow: none;
        }
        
        .spindle {
            width: 16px;
            height: 16px;
            background: radial-gradient(circle, #666 0%, #333 100%);
            border-radius: 50%;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            border: 2px solid #222;
            z-index: 10;
        }
        
        .record-grooves {
            position: absolute;
            top: 10px;
            left: 10px;
            right: 10px;
            bottom: 10px;
            border-radius: 50%;
            background: repeating-radial-gradient(
                circle,
                transparent 0px,
                transparent 2px,
                rgba(255,255,255,0.1) 2px,
                rgba(255,255,255,0.1) 3px
            );
            pointer-events: none;
        }
        
        .tonearm {
            position: absolute;
            top: 20px;
            right: 40px;
            width: 120px;
            height: 8px;
            transform-origin: left center;
            transition: transform 0.3s ease;
            z-index: 5;
        }
        
        .tonearm.playing {
            transform: rotate(-25deg);
        }
        
        .tonearm-base {
            width: 20px;
            height: 20px;
            background: radial-gradient(circle, #666 0%, #333 100%);
            border-radius: 50%;
            border: 2px solid #222;
            position: absolute;
            left: -10px;
            top: 50%;
            transform: translateY(-50%);
        }
        
        .tonearm-pivot {
            width: 8px;
            height: 8px;
            background: #444;
            border-radius: 50%;
            position: absolute;
            left: -4px;
            top: 50%;
            transform: translateY(-50%);
            z-index: 1;
        }
        
        .tonearm-arm {
            width: 100px;
            height: 4px;
            background: linear-gradient(to right, #888 0%, #666 100%);
            border-radius: 2px;
            position: absolute;
            left: 10px;
            top: 50%;
            transform: translateY(-50%);
            box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        
        .cartridge {
            width: 12px;
            height: 8px;
            background: #333;
            border-radius: 2px;
            position: absolute;
            right: -6px;
            top: 50%;
            transform: translateY(-50%);
            border: 1px solid #222;
        }
        
        .cartridge::after {
            content: '';
            width: 1px;
            height: 6px;
            background: #ff0000;
            position: absolute;
            right: -1px;
            top: 1px;
            box-shadow: 0 0 4px #ff0000;
        }
        
        .turntable-controls {
            position: absolute;
            bottom: 15px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .play-pause-btn {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--primary-orange) 0%, #C96D28 100%);
            color: var(--cream);
            border: 3px solid var(--dark-brown);
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        
        .play-pause-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 16px rgba(0,0,0,0.4);
        }
        
        .play-pause-btn:active {
            transform: scale(0.95);
        }
        
        .rpm-indicator {
            font-size: 10px;
            font-weight: 700;
            color: var(--cream);
            background: rgba(139, 69, 19, 0.8);
            padding: 4px 8px;
            border-radius: 4px;
            border: 1px solid var(--dark-brown);
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Pitch Control */
        .pitch-control {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
            margin: 0 15px;
        }
        
        .pitch-label {
            font-size: 10px;
            font-weight: 700;
            color: var(--cream);
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .pitch-slider {
            position: relative;
            width: 80px;
            height: 20px;
            background: var(--knob-black);
            border-radius: 10px;
            border: 2px solid var(--dark-brown);
            cursor: pointer;
        }
        
        .pitch-track {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 1px;
            height: 12px;
            background: var(--primary-orange);
        }
        
        .pitch-thumb {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 12px;
            height: 12px;
            background: radial-gradient(circle at 30% 30%, #E0E0E0, #A0A0A0);
            border: 1px solid var(--knob-black);
            border-radius: 50%;
            transition: all 0.2s ease;
            box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        
        .pitch-readout {
            font-size: 9px;
            font-weight: 700;
            color: var(--primary-orange);
            font-family: 'Courier New', monospace;
            background: var(--knob-black);
            padding: 2px 6px;
            border-radius: 3px;
            border: 1px solid var(--dark-brown);
            min-width: 45px;
            text-align: center;
        }
        
        .knob {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: radial-gradient(circle at 30% 30%, #E0E0E0, #A0A0A0);
            border: 3px solid var(--knob-black);
            position: relative;
            cursor: pointer;
            box-shadow: 
                0 4px 8px rgba(0,0,0,0.4),
                inset 0 2px 4px rgba(255,255,255,0.3);
            transition: all 0.2s ease;
        }
        
        .knob::before {
            content: '';
            position: absolute;
            top: 5px;
            left: 50%;
            transform: translateX(-50%);
            width: 3px;
            height: 15px;
            background: var(--knob-black);
            border-radius: 2px;
        }
        
        .knob:active {
            transform: scale(0.95);
            box-shadow: 
                0 2px 4px rgba(0,0,0,0.6),
                inset 0 2px 4px rgba(0,0,0,0.2);
        }
        
        .nav-button {
            padding: 12px 20px;
            background: linear-gradient(135deg, var(--primary-orange) 0%, #C96D28 100%);
            color: var(--cream);
            border: 2px solid var(--dark-brown);
            border-radius: 8px;
            font-family: 'Courier Prime', monospace;
            font-weight: 700;
            font-size: 14px;
            letter-spacing: 1px;
            text-transform: uppercase;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        
        .nav-button:hover, .nav-button:active {
            background: linear-gradient(135deg, #C96D28 0%, var(--primary-orange) 100%);
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(0,0,0,0.4);
        }
        
        .counter-display {
            background: var(--knob-black);
            color: var(--primary-orange);
            padding: 8px 16px;
            border-radius: 6px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 2px;
            border: 2px solid var(--dark-brown);
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.5);
        }
        
        /* Postcard Display */
        .postcard-container {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px 0;
        }
        
        .postcard {
            width: min(400px, 90vw);
            height: min(280px, 60vw);
            perspective: 1000px;
            margin: 0 auto;
        }
        
        .postcard-inner {
            width: 100%;
            height: 100%;
            transition: transform 0.8s ease-in-out;
            transform-style: preserve-3d;
            position: relative;
            cursor: pointer;
        }
        
        .postcard.flipped .postcard-inner {
            transform: rotateY(180deg);
        }
        
        .postcard-face {
            width: 100%;
            height: 100%;
            position: absolute;
            backface-visibility: hidden;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 
                0 20px 40px rgba(0,0,0,0.3),
                inset 0 0 0 6px var(--cream);
            background: var(--cream);
        }
        
        .postcard-front {
            background: var(--primary-orange);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 30px 20px;
            position: relative;
        }
        
        .postcard-front::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                repeating-linear-gradient(45deg, transparent 0px, transparent 2px, rgba(0,0,0,0.03) 2px, rgba(0,0,0,0.03) 4px),
                radial-gradient(circle at center, rgba(255,255,255,0.1) 0%, transparent 70%);
            pointer-events: none;
        }
        
        .cassette-icon {
            width: 100px;
            height: 70px;
            margin-bottom: 20px;
            z-index: 1;
        }
        
        .cassette-icon svg {
            width: 100%;
            height: 100%;
            filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.4));
        }
        
        .front-title {
            font-size: clamp(20px, 6vw, 32px);
            font-weight: 700;
            color: var(--cream);
            text-shadow: 2px 2px 0 rgba(0,0,0,0.8), 4px 4px 8px rgba(0,0,0,0.4);
            text-align: center;
            letter-spacing: 2px;
            text-transform: uppercase;
            line-height: 0.9;
            z-index: 1;
        }
        
        .postcard-back {
            transform: rotateY(180deg);
            background: var(--cream);
            padding: 20px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
        }
        
        .postcard-back::before {
            content: 'USA 6¢';
            position: absolute;
            top: 15px;
            right: 15px;
            width: 40px;
            height: 25px;
            background: var(--primary-orange);
            color: var(--cream);
            font-size: 8px;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid var(--dark-brown);
        }
        
        .postmark {
            position: absolute;
            top: 15px;
            left: 15px;
            width: 50px;
            height: 50px;
            border: 2px solid rgba(139, 69, 19, 0.6);
            border-radius: 50%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-size: 7px;
            color: rgba(139, 69, 19, 0.8);
            text-align: center;
            background: rgba(139, 69, 19, 0.1);
        }
        
        .back-header {
            font-size: clamp(12px, 4vw, 16px);
            font-weight: 700;
            color: var(--primary-orange);
            text-align: center;
            margin: 40px 0 15px 0;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .music-player {
            width: 100%;
            height: 120px;
            border: 2px solid var(--dark-brown);
            border-radius: 6px;
            background: #000;
            margin-bottom: 15px;
        }
        
        .postcard-note {
            font-size: clamp(10px, 3vw, 12px);
            line-height: 1.4;
            color: var(--dark-brown);
            background: rgba(245, 230, 211, 0.8);
            padding: 10px;
            border-left: 3px solid var(--primary-orange);
            border-radius: 4px;
            text-align: left;
        }
        
        /* Action Buttons */
        .action-buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin: 20px 0;
            flex-wrap: wrap;
        }
        
        .action-btn {
            padding: 10px 16px;
            background: var(--dark-brown);
            color: var(--cream);
            border: none;
            border-radius: 8px;
            font-family: 'Courier Prime', monospace;
            font-weight: 700;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        
        .action-btn:hover, .action-btn:active {
            background: #A0522D;
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(0,0,0,0.4);
        }
        
        /* QR Code Section */
        .qr-section {
            background: rgba(139, 69, 19, 0.9);
            border-radius: 12px;
            padding: 20px;
            margin-top: 20px;
            text-align: center;
        }
        
        .qr-title {
            color: var(--cream);
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        
        .qr-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 15px;
            justify-items: center;
        }
        
        .qr-item {
            background: var(--cream);
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        
        .qr-label {
            font-size: 10px;
            font-weight: 700;
            color: var(--dark-brown);
            margin-top: 8px;
            text-transform: uppercase;
        }
        
        /* Flip Indicator */
        .flip-indicator {
            position: absolute;
            top: 10px;
            right: 10px;
            background: rgba(0,0,0,0.8);
            color: var(--cream);
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            animation: pulse 2s infinite;
            z-index: 10;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 0.7; }
            50% { opacity: 1; }
        }
        
        /* Loading State */
        .loading {
            text-align: center;
            color: var(--primary-orange);
            font-size: 18px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        
        /* Responsive Design */
        @media (max-width: 480px) {
            .control-row {
                gap: 10px;
            }
            .knob {
                width: 40px;
                height: 40px;
            }
            .nav-button {
                padding: 8px 12px;
                font-size: 12px;
            }
            .music-player {
                height: 100px;
            }
        }
        
        @media (orientation: landscape) and (max-height: 600px) {
            .app-container {
                padding: 10px;
            }
            .postcard {
                height: min(200px, 40vh);
            }
            .music-player {
                height: 80px;
            }
        }
        
        /* Print Styles */
        @media print {
            .no-print {
                display: none !important;
            }
            body {
                background: white;
            }
            .postcard {
                page-break-after: always;
            }
        }
        
        /* Control Console - Patch Bay Style */
        .control-console {
            background: 
                radial-gradient(circle at 25% 25%, rgba(0,0,0,0.7) 2px, transparent 2px),
                radial-gradient(circle at 75% 75%, rgba(0,0,0,0.5) 1px, transparent 1px),
                radial-gradient(circle at 30% 80%, rgba(0,0,0,0.4) 1px, transparent 1px),
                radial-gradient(circle at 70% 30%, rgba(0,0,0,0.6) 2px, transparent 2px),
                radial-gradient(circle at 50% 50%, rgba(139, 69, 19, 0.2) 0%, transparent 70%),
                linear-gradient(135deg, #654321 0%, #3E2723 25%, #2E1B13 50%, #1E0E0A 75%, #0A0502 100%);
            border: 4px solid rgba(101, 67, 33, 0.8);
            border-radius: 16px;
            padding: 25px;
            margin: 20px 0;
            position: relative;
            overflow: hidden;
            box-shadow: 
                0 8px 24px rgba(0,0,0,0.6),
                inset 0 3px 0 rgba(255,255,255,0.1),
                inset 0 -3px 0 rgba(0,0,0,0.5);
        }
        
        .control-console::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                linear-gradient(45deg, transparent 0%, transparent 47%, rgba(0,0,0,0.08) 48%, rgba(0,0,0,0.08) 52%, transparent 53%),
                repeating-linear-gradient(90deg, 
                    transparent 0px, 
                    transparent 4px, 
                    rgba(0,0,0,0.02) 4px, 
                    rgba(0,0,0,0.02) 8px
                );
            border-radius: 16px;
            pointer-events: none;
        }
        
        .console-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
            padding: 10px 15px;
            background: rgba(0,0,0,0.3);
            border-radius: 8px;
            border: 2px solid rgba(101, 67, 33, 0.6);
        }
        
        .console-label, .qr-console-label {
            font-size: 11px;
            font-weight: 700;
            color: var(--cream);
            text-transform: uppercase;
            letter-spacing: 1px;
            font-family: 'Courier Prime', monospace;
        }
        
        .led-strip, .qr-led-strip {
            display: flex;
            gap: 8px;
            align-items: center;
        }
        
        .status-led, .qr-status-led {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #333;
            border: 1px solid #666;
            box-shadow: inset 0 1px 2px rgba(0,0,0,0.5);
            transition: all 0.3s ease;
        }
        
        .status-led.active, .qr-status-led.active {
            background: #00ff00;
            border-color: #00cc00;
            box-shadow: 
                inset 0 1px 2px rgba(0,0,0,0.3),
                0 0 8px #00ff00,
                0 0 16px rgba(0,255,0,0.3);
        }
        
        .status-led.warning, .qr-status-led.warning {
            background: #ffaa00;
            border-color: #cc8800;
            box-shadow: 
                inset 0 1px 2px rgba(0,0,0,0.3),
                0 0 8px #ffaa00,
                0 0 16px rgba(255,170,0,0.3);
        }
        
        .status-led.danger, .qr-status-led.danger {
            background: #ff0000;
            border-color: #cc0000;
            box-shadow: 
                inset 0 1px 2px rgba(0,0,0,0.3),
                0 0 8px #ff0000,
                0 0 16px rgba(255,0,0,0.3);
        }
        
        .console-controls {
            display: flex;
            justify-content: space-around;
            align-items: center;
            gap: 20px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }
        
        .control-group {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
        }
        
        .control-knob {
            width: 50px;
            height: 50px;
            position: relative;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        
        .knob-chrome {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: 
                radial-gradient(circle at 25% 25%, #ffffff 0%, #f0f0f0 15%, #d0d0d0 30%, #b0b0b0 50%, #909090 70%, #707070 85%, #505050 100%);
            border: 4px solid #1a1a1a;
            box-shadow: 
                0 6px 12px rgba(0,0,0,0.6),
                inset 0 3px 6px rgba(255,255,255,0.4),
                inset 0 -3px 6px rgba(0,0,0,0.3);
            position: relative;
        }
        
        .knob-indicator {
            position: absolute;
            top: 8px;
            left: 50%;
            transform: translateX(-50%);
            width: 4px;
            height: 16px;
            background: linear-gradient(to bottom, #000 0%, #333 100%);
            border-radius: 2px;
            box-shadow: 
                inset 0 1px 2px rgba(0,0,0,0.8),
                0 1px 0 rgba(255,255,255,0.3);
        }
        
        .control-knob:hover .knob-chrome {
            transform: scale(1.05);
            box-shadow: 
                0 8px 16px rgba(0,0,0,0.7),
                inset 0 3px 6px rgba(255,255,255,0.5),
                inset 0 -3px 6px rgba(0,0,0,0.4);
        }
        
        .control-knob:active .knob-chrome {
            transform: scale(0.95);
        }
        
        .control-label {
            font-size: 9px;
            font-weight: 700;
            color: var(--cream);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            text-align: center;
            font-family: 'Courier Prime', monospace;
        }
        
        .sub-label {
            font-size: 7px;
            opacity: 0.8;
            display: block;
            margin-top: 2px;
        }
        
        /* QR Console Section */
        .qr-console-section {
            background: rgba(0,0,0,0.2);
            border: 3px solid rgba(101, 67, 33, 0.6);
            border-radius: 12px;
            padding: 20px;
            position: relative;
        }
        
        .qr-console-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                repeating-linear-gradient(45deg, 
                    transparent 0px, 
                    transparent 6px, 
                    rgba(139, 69, 19, 0.01) 6px, 
                    rgba(139, 69, 19, 0.01) 12px
                );
            border-radius: 12px;
            pointer-events: none;
        }
        
        .qr-console-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 15px;
            padding: 8px 12px;
            background: rgba(0,0,0,0.4);
            border-radius: 6px;
            border: 2px solid rgba(101, 67, 33, 0.4);
        }
        
        .qr-grid-console {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
            gap: 12px;
            justify-items: center;
        }
        
        .qr-item {
            background: 
                radial-gradient(circle at 30% 30%, rgba(245, 230, 211, 0.95) 0%, rgba(235, 220, 201, 0.9) 100%);
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 
                0 4px 12px rgba(0,0,0,0.4),
                inset 0 1px 0 rgba(255,255,255,0.2);
            border: 2px solid rgba(139, 69, 19, 0.6);
            position: relative;
            transition: all 0.3s ease;
        }
        
        .qr-item:hover {
            transform: translateY(-2px);
            box-shadow: 
                0 6px 16px rgba(0,0,0,0.5),
                inset 0 1px 0 rgba(255,255,255,0.3);
        }
        
        .qr-item::before {
            content: '';
            position: absolute;
            top: 3px;
            right: 3px;
            width: 6px;
            height: 6px;
            background: #00ff00;
            border-radius: 50%;
            box-shadow: 0 0 4px rgba(0,255,0,0.6);
            opacity: 0.8;
        }
        
        .qr-label {
            font-size: 8px;
            font-weight: 700;
            color: var(--dark-brown);
            margin-top: 6px;
            text-transform: uppercase;
            font-family: 'Courier Prime', monospace;
            letter-spacing: 0.5px;
        }
        @media (prefers-color-scheme: dark) {
            :root {
                --cream: #f0f0f0;
            }
        }
        
        /* Dedication */
        .dedication {
            text-align: center;
            font-size: 9px;
            font-style: italic;
            color: rgba(139, 69, 19, 0.6);
            margin-top: 30px;
            padding: 15px;
            font-family: 'Courier Prime', monospace;
            letter-spacing: 0.5px;
            line-height: 1.3;
        }
    </style>
    <noscript>
        <div style="text-align: center; color: #ff4444; font-size: 24px; padding: 20px;">
            Enable JavaScript to run this app – the funk don't flow without it, fam.
        </div>
    </noscript>
</head>
<body>
    <div class="app-container">
        <header class="app-header">
            <div class="patch-bay-title">
                <div class="led-word">
                    <div class="led-letter" data-letter="C"></div>
                    <div class="led-letter" data-letter="R"></div>
                    <div class="led-letter" data-letter="A"></div>
                    <div class="led-letter" data-letter="T"></div>
                    <div class="led-letter" data-letter="E"></div>
                </div>
                <div class="led-word">
                    <div class="led-letter" data-letter="J"></div>
                    <div class="led-letter" data-letter="U"></div>
                    <div class="led-letter" data-letter="I"></div>
                    <div class="led-letter" data-letter="C"></div>
                    <div class="led-letter" data-letter="E"></div>
                </div>
            </div>
            <p class="app-subtitle">SONIC LOVE CARDS FROM THE OVERGROUND</p>
        </header>
        
        <div class="mixing-panel no-print">
            <!-- Top Row - Channel EQ and Controls -->
            <div class="channel-strip">
                <div class="channel" data-channel="1">
                    <div class="channel-label">CH 1</div>
                    <div class="led-indicator active" id="ch1-led"></div>
                    <div class="eq-section">
                        <div class="eq-knob-group">
                            <label>HI</label>
                            <div class="eq-knob" data-eq="hi"></div>
                        </div>
                        <div class="eq-knob-group">
                            <label>MID</label>
                            <div class="eq-knob" data-eq="mid"></div>
                        </div>
                        <div class="eq-knob-group">
                            <label>LOW</label>
                            <div class="eq-knob" data-eq="low"></div>
                        </div>
                    </div>
                    <div class="gain-knob-group">
                        <label>GAIN</label>
                        <div class="gain-knob"></div>
                    </div>
                    <div class="vu-meter">
                        <div class="vu-bar" id="vu-left-1"></div>
                        <div class="vu-bar" id="vu-right-1"></div>
                    </div>
                </div>
                
                <div class="channel" data-channel="2">
                    <div class="channel-label">CH 2</div>
                    <div class="led-indicator" id="ch2-led"></div>
                    <div class="eq-section">
                        <div class="eq-knob-group">
                            <label>HI</label>
                            <div class="eq-knob" data-eq="hi"></div>
                        </div>
                        <div class="eq-knob-group">
                            <label>MID</label>
                            <div class="eq-knob" data-eq="mid"></div>
                        </div>
                        <div class="eq-knob-group">
                            <label>LOW</label>
                            <div class="eq-knob" data-eq="low"></div>
                        </div>
                    </div>
                    <div class="gain-knob-group">
                        <label>GAIN</label>
                        <div class="gain-knob"></div>
                    </div>
                    <div class="vu-meter">
                        <div class="vu-bar" id="vu-left-2"></div>
                        <div class="vu-bar" id="vu-right-2"></div>
                    </div>
                </div>
            </div>
            
            <!-- Main Controls -->
            <div class="control-row">
                <div class="knob" id="prev-knob" title="Previous Track"></div>
                <button class="nav-button" id="prev-btn">◀ PREV</button>
                <div class="counter-display" id="counter">LOADING...</div>
                <button class="nav-button" id="next-btn">NEXT ▶</button>
                <div class="knob" id="next-knob" title="Next Track"></div>
            </div>
            
            <!-- Pitch and Crossfader -->
            <div class="control-row">
                <div class="pitch-control">
                    <div class="pitch-label">PITCH</div>
                    <div class="pitch-slider">
                        <div class="pitch-track"></div>
                        <div class="pitch-thumb" id="pitch-thumb"></div>
                    </div>
                    <div class="pitch-readout">PLr +0%</div>
                </div>
                
                <div class="crossfader-control">
                    <div class="crossfader-label">CROSSFADER</div>
                    <div class="crossfader-slider">
                        <div class="crossfader-track"></div>
                        <div class="crossfader-thumb" id="crossfader-thumb"></div>
                    </div>
                </div>
            </div>
            
            <!-- Stem Separation Controls -->
            <div class="turntable-section">
                <div class="turntable-container">
                    <div class="turntable-base">
                        <div class="strobe-light">
                            <div class="strobe-dots">
                                <div class="strobe-dot"></div>
                                <div class="strobe-dot"></div>
                                <div class="strobe-dot"></div>
                                <div class="strobe-dot"></div>
                            </div>
                        </div>
                        <div class="platter" id="platter">
                            <div class="record-label">
                                <div class="postcard-vinyl" id="postcard-vinyl">
                                    <div class="vinyl-content" id="vinyl-content">
                                        <div class="cassette-icon">
                                            <svg viewBox="0 0 100 70" fill="none">
                                                <rect x="5" y="15" width="90" height="40" rx="6" fill="var(--cream)" stroke="var(--dark-brown)" stroke-width="2"/>
                                                <circle cx="25" cy="35" r="10" fill="none" stroke="var(--dark-brown)" stroke-width="2"/>
                                                <circle cx="75" cy="35" r="10" fill="none" stroke="var(--dark-brown)" stroke-width="2"/>
                                                <rect x="35" y="27" width="30" height="16" rx="2" fill="var(--dark-brown)"/>
                                                <rect x="15" y="50" width="70" height="3" rx="1" fill="var(--dark-brown)"/>
                                            </svg>
                                        </div>
                                        <div class="vinyl-title" id="vinyl-title">SONIC<br>POSTCARD</div>
                                    </div>
                                </div>
                                <div class="spindle"></div>
                            </div>
                            <div class="record-grooves"></div>
                        </div>
                        <div class="tonearm" id="tonearm">
                            <div class="tonearm-base"></div>
                            <div class="tonearm-pivot"></div>
                            <div class="tonearm-arm"></div>
                            <div class="cartridge"></div>
                        </div>
                        <div class="turntable-controls">
                            <button class="play-pause-btn" id="play-pause-btn">▶</button>
                            <div class="rpm-indicator">33⅓ RPM</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="postcard-container">
            <div id="loading" class="loading">LOADING SONIC POSTCARD...</div>
            
            <div class="postcard" id="postcard" style="display: none;">
                <div class="postcard-inner">
                    <div class="postcard-face postcard-front">
                        <div class="cassette-icon">
                            <svg viewBox="0 0 100 70" fill="none">
                                <rect x="5" y="15" width="90" height="40" rx="6" fill="var(--cream)" stroke="var(--dark-brown)" stroke-width="2"/>
                                <circle cx="25" cy="35" r="10" fill="none" stroke="var(--dark-brown)" stroke-width="2"/>
                                <circle cx="75" cy="35" r="10" fill="none" stroke="var(--dark-brown)" stroke-width="2"/>
                                <rect x="35" y="27" width="30" height="16" rx="2" fill="var(--dark-brown)"/>
                                <rect x="15" y="50" width="70" height="3" rx="1" fill="var(--dark-brown)"/>
                                <circle cx="20" cy="60" r="1.5" fill="var(--dark-brown)"/>
                                <circle cx="30" cy="60" r="1.5" fill="var(--dark-brown)"/>
                                <circle cx="70" cy="60" r="1.5" fill="var(--dark-brown)"/>
                                <circle cx="80" cy="60" r="1.5" fill="var(--dark-brown)"/>
                            </svg>
                        </div>
                        <div class="front-title" id="front-title">SONIC<br>POSTCARD</div>
                        <div class="flip-indicator">TAP TO FLIP</div>
                    </div>
                    
                    <div class="postcard-face postcard-back">
                        <div class="postmark">
                            <div>NYC</div>
                            <div>SEP</div>
                            <div>24</div>
                        </div>
                        
                        <h3 class="back-header" id="back-header">SONIC POSTCARD FROM JUICE</h3>
                        
                        <iframe class="music-player" id="music-player" src="" frameborder="0" 
                                allow="autoplay; encrypted-media" allowfullscreen></iframe>
                        
                        <div class="postcard-note" id="postcard-note">Loading message...</div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="action-buttons no-print">
            <button class="action-btn" id="flip-btn">FLIP CARD</button>
            <button class="action-btn" id="share-btn">SHARE</button>
            <button class="action-btn" onclick="window.print()">PRINT</button>
        </div>
        
        <div class="qr-section no-print">
            <h3 class="qr-title">QR Codes - All Postcards</h3>
            <div class="qr-grid" id="qr-grid"></div>
        </div>
        
        <div class="dedication">
            love always to Mmi & Cbo! + thank you.<br>-juice xo
        </div>
    </div>

    <script>
        // Postcard Data
        const postcards = [
            {
                id: 1,
                frontTitle: "TAPE<br>DECK",
                backHeader: "ANALOG SESSIONS",
                track: 'https://www.youtube.com/embed/Q22MCFC0CP0',
                note: 'Found this buried in the B-side collection. That warm analog saturation hits different when the lights are low. Turn it up and let it ride. - J'
            },
            {
                id: 2,
                frontTitle: "MIX<br>TAPE",
                backHeader: "UNDERGROUND TRANSMISSION",
                track: 'https://www.youtube.com/embed/ISV--pePI7M',
                note: 'Side B of that lost session from 85. The kind of track that stops conversations and makes you lean into the speakers. Raw and unfiltered. - Juice'
            },
            {
                id: 3,
                frontTitle: "BOOM<br>BOX",
                backHeader: "STREET CORNER SOUNDTRACK",
                track: 'https://www.youtube.com/embed/_jgpVF9uZjQ',
                note: '"bare bones" - Juice. Sometimes thats all you need. No studio tricks, no digital polish. Just the music in its purest form. Feel that? - J'
            },
            {
                id: 4,
                frontTitle: "HEAD<br>PHONES",
                backHeader: "LATE NIGHT LISTENING",
                track: 'https://www.youtube.com/embed/fM2YkUnaKR8',
                note: 'This one came through the static at 3AM. Had to dig through 200 records to track it down. Worth every minute of searching the crates. - Juice'
            },
            {
                id: 5,
                frontTitle: "TURN<br>TABLE",
                backHeader: "VINYL ONLY SPECIAL",
                track: 'https://www.youtube.com/embed/tCnBrrnOefs',
                note: 'Dusty fingers, needle drops, and that moment when the beat drops. This is what crate digging is about. Pure sonic archaeology. - J'
            },
            {
                id: 6,
                frontTitle: "STUDIO<br>MONITOR",
                backHeader: "REFERENCE TRACK",
                track: 'https://www.youtube.com/embed/CZe9YxJNs48',
                note: 'Engineer said this never made it to the pressing plant. Found the master tape in a forgotten box. Sometimes the best music never sees daylight. - Juice'
            },
            {
                id: 7,
                frontTitle: "REEL TO<br>REEL",
                backHeader: "ARCHIVE DISCOVERY",
                track: 'https://www.youtube.com/embed/qcZ7e9EOQTY',
                note: 'Quarter inch tape, 15 IPS, recorded live to 2-track. The way music used to be captured - with intention, in the moment, no second chances. - J'
            },
            {
                id: 8,
                frontTitle: "RADIO<br>WAVES",
                backHeader: "BROADCAST RARE",
                track: 'https://www.youtube.com/embed/pa14VNsdSYM',
                note: 'Caught this on late night FM years ago. Never heard it again until now. Sometimes the airwaves deliver magic when youre not looking. - Juice'
            },
            {
                id: 9,
                frontTitle: "SPOTIFY<br>STREAM",
                backHeader: "PLAYLIST SPECIAL",
                track: 'https://open.spotify.com/embed/track/4iV5W9uYEdYUVa79Axb7Rh',
                trackType: 'spotify',
                note: 'Fresh from the underground playlist. This track captures that raw energy we chase in the crates. Stream it, feel it, live it. - Juice'
            }
        ];
        
        // App State
        let currentIndex = 0;
        let currentPostcard = postcards[0];
        let audioContext = null;
        let analyser = null;
        let sourceNode = null;
        let isPlaying = false;
        
        // Initialize Web Audio API
        function initAudioContext() {
            if (!audioContext) {
                audioContext = new (window.AudioContext || window.webkitAudioContext)();
                analyser = audioContext.createAnalyser();
                analyser.fftSize = 256;
            }
        }
        
        // VU Meter Animation
        function updateVUMeters() {
            if (!analyser) return;
            
            const dataArray = new Uint8Array(analyser.frequencyBinCount);
            analyser.getByteFrequencyData(dataArray);
            
            // Calculate average amplitude for left/right channels (simulated)
            const leftLevel = Math.max(...dataArray.slice(0, dataArray.length / 2)) / 255;
            const rightLevel = Math.max(...dataArray.slice(dataArray.length / 2)) / 255;
            
            // Update VU bars
            updateVUBar('vu-left-1', leftLevel);
            updateVUBar('vu-right-1', rightLevel);
            updateVUBar('vu-left-2', leftLevel * 0.7); // Simulate second channel
            updateVUBar('vu-right-2', rightLevel * 0.7);
            
            // Update LEDs based on levels
            updateLEDs(Math.max(leftLevel, rightLevel));
            
            requestAnimationFrame(updateVUMeters);
        }
        
        function updateVUBar(elementId, level) {
            const bar = document.getElementById(elementId);
            if (bar) {
                const fill = Math.min(100, level * 100);
                bar.style.background = `linear-gradient(to top, 
                    ${fill > 85 ? '#ff0000' : fill > 75 ? '#ff8800' : fill > 60 ? '#ffff00' : '#00ff00'} ${fill}%, 
                    #333 ${fill}%)`;
            }
        }
        
        function updateLEDs(level) {
            const ch1Led = document.getElementById('ch1-led');
            const ch2Led = document.getElementById('ch2-led');
            
            // Remove all LED states
            [ch1Led, ch2Led].forEach(led => {
                if (led) led.classList.remove('active', 'warning', 'danger');
            });
            
            // Set LED state based on audio level
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
        
        // Simulate VU meters with random data when no real audio
        function simulateVUMeters() {
            if (isPlaying) {
                const baseLevel = 0.3 + Math.random() * 0.4; // Base level with variation
                const leftLevel = Math.min(1, baseLevel + (Math.random() - 0.5) * 0.3);
                const rightLevel = Math.min(1, baseLevel + (Math.random() - 0.5) * 0.3);
                
                updateVUBar('vu-left-1', leftLevel);
                updateVUBar('vu-right-1', rightLevel);
                updateVUBar('vu-left-2', leftLevel * 0.8);
                updateVUBar('vu-right-2', rightLevel * 0.8);
                updateLEDs(Math.max(leftLevel, rightLevel));
            } else {
                // Fade out when not playing
                updateVUBar('vu-left-1', 0);
                updateVUBar('vu-right-1', 0);
                updateVUBar('vu-left-2', 0);
                updateVUBar('vu-right-2', 0);
                updateLEDs(0);
            }
            
            setTimeout(simulateVUMeters, 100);
        }
        
        // Turntable Controls
        function initTurntable() {
            const playPauseBtn = document.getElementById('play-pause-btn');
            const platter = document.getElementById('platter');
            const tonearm = document.getElementById('tonearm');
            
            if (playPauseBtn) {
                playPauseBtn.addEventListener('click', togglePlayback);
            }
            
            // Update vinyl content when postcard changes
            updateVinylContent();
        }
        
        function updateVinylContent() {
            const vinylTitle = document.getElementById('vinyl-title');
            const vinylContent = document.getElementById('vinyl-content');
            
            if (vinylTitle && currentPostcard) {
                vinylTitle.innerHTML = currentPostcard.frontTitle;
            }
        }
        
        function togglePlayback() {
            isPlaying = !isPlaying;
            const playPauseBtn = document.getElementById('play-pause-btn');
            const platter = document.getElementById('platter');
            const tonearm = document.getElementById('tonearm');
            
            if (isPlaying) {
                // Start playing
                playPauseBtn.textContent = '⏸';
                platter.classList.add('spinning');
                tonearm.classList.add('playing');
                
                // Start YouTube video if available
                const musicPlayer = document.getElementById('music-player');
                if (musicPlayer && musicPlayer.contentWindow) {
                    try {
                        // Send play command to YouTube embed
                        musicPlayer.contentWindow.postMessage('{"event":"command","func":"playVideo","args":""}', '*');
                    } catch (e) {
                        console.log('YouTube control not available');
                    }
                }
                
                hapticFeedback('medium');
                showToast('NOW PLAYING');
                
            } else {
                // Pause
                playPauseBtn.textContent = '▶';
                platter.classList.remove('spinning');
                tonearm.classList.remove('playing');
                
                // Pause YouTube video if available
                const musicPlayer = document.getElementById('music-player');
                if (musicPlayer && musicPlayer.contentWindow) {
                    try {
                        musicPlayer.contentWindow.postMessage('{"event":"command","func":"pauseVideo","args":""}', '*');
                    } catch (e) {
                        console.log('YouTube control not available');
                    }
                }
                
                hapticFeedback('light');
                showToast('PAUSED');
            }
        }
        
        // EQ Knob Controls
        function initEQKnobs() {
            document.querySelectorAll('.eq-knob, .gain-knob').forEach(knob => {
                knob.addEventListener('mousedown', startKnobDrag);
                knob.addEventListener('touchstart', startKnobDrag, { passive: false });
            });
        }
        
        function startKnobDrag(e) {
            e.preventDefault();
            const knob = e.target;
            const rect = knob.getBoundingClientRect();
            const centerX = rect.left + rect.width / 2;
            const centerY = rect.top + rect.height / 2;
            
            let currentRotation = parseInt(knob.dataset.rotation || 0);
            
            function updateKnob(clientX, clientY) {
                const angle = Math.atan2(clientY - centerY, clientX - centerX);
                const degrees = (angle * 180 / Math.PI + 90) % 360;
                const snappedDegrees = Math.round(degrees / 15) * 15; // 15-degree increments
                
                knob.style.transform = `rotate(${snappedDegrees}deg)`;
                knob.dataset.rotation = snappedDegrees;
                
                // Haptic feedback
                if (Math.abs(snappedDegrees - currentRotation) >= 15) {
                    hapticFeedback('light');
                    currentRotation = snappedDegrees;
                }
            }
            
            function handleMove(e) {
                const clientX = e.clientX || (e.touches && e.touches[0].clientX);
                const clientY = e.clientY || (e.touches && e.touches[0].clientY);
                updateKnob(clientX, clientY);
            }
            
            function handleEnd() {
                document.removeEventListener('mousemove', handleMove);
                document.removeEventListener('mouseup', handleEnd);
                document.removeEventListener('touchmove', handleMove);
                document.removeEventListener('touchend', handleEnd);
            }
            
            document.addEventListener('mousemove', handleMove);
            document.addEventListener('mouseup', handleEnd);
            document.addEventListener('touchmove', handleMove, { passive: false });
            document.addEventListener('touchend', handleEnd);
        }
        
        // Pitch Control - Vertical
        function initPitchControl() {
            const pitchSlider = document.querySelector('.pitch-slider-vertical');
            const pitchThumb = document.getElementById('pitch-thumb-vertical');
            const pitchReadout = document.querySelector('.pitch-readout-vertical');
            
            if (!pitchSlider || !pitchThumb || !pitchReadout) return;
            
            let pitchValue = 0; // -50 to +50
            
            pitchSlider.addEventListener('mousedown', handlePitchDrag);
            pitchSlider.addEventListener('touchstart', handlePitchDrag, { passive: false });
            
            function handlePitchDrag(e) {
                e.preventDefault();
                const rect = pitchSlider.getBoundingClientRect();
                
                function updatePitch(clientY) {
                    const y = Math.max(0, Math.min(rect.height, clientY - rect.top));
                    const percentage = 1 - (y / rect.height); // Inverted for vertical
                    pitchValue = Math.round((percentage - 0.5) * 100); // -50 to +50
                    
                    pitchThumb.style.top = `${(1 - percentage) * 100}%`;
                    pitchReadout.textContent = `PLr ${pitchValue >= 0 ? '+' : ''}${pitchValue}%`;
                    
                    hapticFeedback('light');
                }
                
                function handleMove(e) {
                    const clientY = e.clientY || (e.touches && e.touches[0].clientY);
                    updatePitch(clientY);
                }
                
                function handleEnd() {
                    document.removeEventListener('mousemove', handleMove);
                    document.removeEventListener('mouseup', handleEnd);
                    document.removeEventListener('touchmove', handleMove);
                    document.removeEventListener('touchend', handleEnd);
                }
                
                updatePitch(e.clientY || e.touches[0].clientY);
                
                document.addEventListener('mousemove', handleMove);
                document.addEventListener('mouseup', handleEnd);
                document.addEventListener('touchmove', handleMove, { passive: false });
                document.addEventListener('touchend', handleEnd);
            }
        }
        
        // Crossfader Control
        function initCrossfader() {
            const crossfaderSlider = document.querySelector('.crossfader-slider');
            const crossfaderThumb = document.getElementById('crossfader-thumb');
            
            crossfaderSlider.addEventListener('mousedown', handleCrossfaderDrag);
            crossfaderSlider.addEventListener('touchstart', handleCrossfaderDrag, { passive: false });
            
            function handleCrossfaderDrag(e) {
                e.preventDefault();
                const rect = crossfaderSlider.getBoundingClientRect();
                
                function updateCrossfader(clientX) {
                    const x = Math.max(0, Math.min(rect.width, clientX - rect.left));
                    const percentage = x / rect.width;
                    
                    crossfaderThumb.style.left = `${percentage * 100}%`;
                    
                    // Update channel volumes based on crossfader position
                    const ch1Volume = percentage < 0.5 ? 1 : (1 - percentage) * 2;
                    const ch2Volume = percentage > 0.5 ? 1 : percentage * 2;
                    
                    hapticFeedback('light');
                }
                
                function handleMove(e) {
                    const clientX = e.clientX || (e.touches && e.touches[0].clientX);
                    updateCrossfader(clientX);
                }
                
                function handleEnd() {
                    document.removeEventListener('mousemove', handleMove);
                    document.removeEventListener('mouseup', handleEnd);
                    document.removeEventListener('touchmove', handleMove);
                    document.removeEventListener('touchend', handleEnd);
                }
                
                updateCrossfader(e.clientX || e.touches[0].clientX);
                
                document.addEventListener('mousemove', handleMove);
                document.addEventListener('mouseup', handleEnd);
                document.addEventListener('touchmove', handleMove, { passive: false });
                document.addEventListener('touchend', handleEnd);
            }
        }
        
        // Stem Separation (Mock Implementation)
        function initStemControls() {
            document.querySelectorAll('.stem-btn').forEach(btn => {
                btn.addEventListener('click', handleStemToggle);
            });
            
            document.getElementById('download-stems').addEventListener('click', handleStemDownload);
        }
        
        function handleStemToggle(e) {
            const btn = e.target;
            const stem = btn.dataset.stem;
            
            // Toggle stem state
            stemStates[stem] = !stemStates[stem];
            btn.classList.toggle('active', stemStates[stem]);
            
            // Mock processing animation
            btn.classList.add('processing');
            setTimeout(() => {
                btn.classList.remove('processing');
            }, 1000);
            
            hapticFeedback('medium');
            
            // Show toast with stem status
            showToast(`${stem.toUpperCase()}: ${stemStates[stem] ? 'ISOLATED' : 'MUTED'}`);
        }
        
        async function handleStemDownload() {
            const activeStemsCount = Object.values(stemStates).filter(Boolean).length;
            
            if (activeStemsCount === 0) {
                showToast('SELECT STEMS TO DOWNLOAD');
                return;
            }
            
            // Show processing state
            const downloadBtn = document.getElementById('download-stems');
            const originalText = downloadBtn.textContent;
            downloadBtn.textContent = 'PROCESSING...';
            downloadBtn.disabled = true;
            
            try {
                // Mock processing delay
                await new Promise(resolve => setTimeout(resolve, 3000));
                
                // In a real implementation, this would:
                // 1. Send audio to a stem separation service (Spleeter, Demucs, etc.)
                // 2. Process the separated stems
                // 3. Generate downloadable MP3 files
                
                const activeStem = Object.keys(stemStates).find(key => stemStates[key]);
                if (activeStem) {
                    // Mock download trigger
                    const link = document.createElement('a');
                    link.href = 'data:audio/mp3;base64,'; // Mock MP3 data
                    link.download = `cratejuice-${currentPostcard.id}-${activeStem}.mp3`;
                    
                    showToast(`DOWNLOAD READY: ${activeStem.toUpperCase()} STEM`);
                }
                
            } catch (error) {
                console.error('Stem separation failed:', error);
                showToast('PROCESSING FAILED - TRY AGAIN');
            } finally {
                downloadBtn.textContent = originalText;
                downloadBtn.disabled = false;
            }
        }
        
        // Navigation
        function loadPostcard(index) {
            currentIndex = index;
            currentPostcard = postcards[index];
            
            // Update content
            const frontTitle = document.getElementById('front-title');
            const backHeader = document.getElementById('back-header');
            const musicPlayer = document.getElementById('music-player');
            const postcardNote = document.getElementById('postcard-note');
            const counter = document.getElementById('counter');
            const loading = document.getElementById('loading');
            const postcard = document.getElementById('postcard');
            
            if (frontTitle) frontTitle.innerHTML = currentPostcard.frontTitle;
            if (backHeader) backHeader.textContent = currentPostcard.backHeader;
            if (musicPlayer) musicPlayer.src = currentPostcard.track + '?autoplay=0&enablejsapi=1';
            if (postcardNote) postcardNote.textContent = currentPostcard.note;
            if (counter) counter.textContent = `TRACK ${index + 1} OF ${postcards.length}`;
            
            // Update vinyl content
            updateVinylContent();
            
            // Update URL
            const newUrl = `${window.location.origin}${window.location.pathname}?id=${currentPostcard.id}`;
            history.replaceState(null, '', newUrl);
            
            // Reset flip state and playback
            if (postcard) {
                postcard.classList.remove('flipped');
            }
            
            // Reset playback state
            if (isPlaying) {
                isPlaying = false;
                const playPauseBtn = document.getElementById('play-pause-btn');
                const platter = document.getElementById('platter');
                const tonearm = document.getElementById('tonearm');
                
                if (playPauseBtn) playPauseBtn.textContent = '▶';
                if (platter) platter.classList.remove('spinning');
                if (tonearm) tonearm.classList.remove('playing');
            }
            
            // Show postcard, hide loading
            if (loading) loading.style.display = 'none';
            if (postcard) postcard.style.display = 'block';
        }
        
        function nextPostcard() {
            currentIndex = (currentIndex + 1) % postcards.length;
            loadPostcard(currentIndex);
            animateKnob('next-knob');
        }
        
        function prevPostcard() {
            currentIndex = (currentIndex - 1 + postcards.length) % postcards.length;
            loadPostcard(currentIndex);
            animateKnob('prev-knob');
        }
        
        function flipPostcard() {
            const postcard = document.getElementById('postcard');
            if (postcard) {
                postcard.classList.toggle('flipped');
            }
        }
        
        function animateKnob(knobId) {
            const knob = document.getElementById(knobId);
            if (knob) {
                knob.style.transform = 'scale(0.9) rotate(45deg)';
                setTimeout(() => {
                    knob.style.transform = 'scale(1) rotate(0deg)';
                }, 150);
            }
        }
        
        // QR Code Generation
        function generateQRCodes() {
            const qrGrid = document.getElementById('qr-grid');
            if (!qrGrid) return;
            
            qrGrid.innerHTML = '';
            
            postcards.forEach((postcard, index) => {
                const qrItem = document.createElement('div');
                qrItem.className = 'qr-item';
                
                const qrDiv = document.createElement('div');
                const url = `${window.location.origin}${window.location.pathname}?id=${postcard.id}`;
                
                try {
                    new QRCode(qrDiv, {
                        text: url,
                        width: 100,
                        height: 100;
                        colorDark: "#8b4513",
                        colorLight: "#f5e6d3",
                        correctLevel: QRCode.CorrectLevel.H
                    });
                } catch (error) {
                    qrDiv.innerHTML = '<div style="width:100px;height:100px;background:#ddd;display:flex;align-items:center;justify-content:center;font-size:10px;">QR ERROR</div>';
                }
                
                const label = document.createElement('div');
                label.className = 'qr-label';
                label.textContent = `TRACK ${index + 1}`;
                
                qrItem.appendChild(qrDiv);
                qrItem.appendChild(label);
                qrGrid.appendChild(qrItem);
            });
        }
        
        // Share functionality
        function fallbackShare(shareData) {
            if (navigator.clipboard) {
                navigator.clipboard.writeText(shareData.url).then(() => {
                    showToast('Link copied to clipboard!');
                });
            } else {
                const textArea = document.createElement('textarea');
                textArea.value = shareData.url;
                document.body.appendChild(textArea);
                textArea.select();
                document.execCommand('copy');
                document.body.removeChild(textArea);
                showToast('Link copied to clipboard!');
            }
        }
        
        function showToast(message) {
            const toast = document.createElement('div');
            toast.style.cssText = `
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: var(--dark-brown);
                color: var(--cream);
                padding: 12px 20px;
                border-radius: 8px;
                font-family: 'Courier Prime', monospace;
                font-weight: 700;
                font-size: 14px;
                z-index: 1000;
                box-shadow: 0 8px 24px rgba(0,0,0,0.4);
            `;
            toast.textContent = message;
            document.body.appendChild(toast);
            
            setTimeout(() => {
                toast.style.opacity = '0';
                toast.style.transition = 'opacity 0.3s ease';
                setTimeout(() => {
                    if (document.body.contains(toast)) {
                        document.body.removeChild(toast);
                    }
                }, 300);
            }, 2000);
        }
        
        // Add haptic feedback function
        function hapticFeedback(type = 'light') {
            if ('vibrate' in navigator) {
                const patterns = {
                    light: [10],
                    medium: [20],
                    heavy: [30]
                };
                navigator.vibrate(patterns[type] || patterns.light);
            }
        }
        
        // Enhanced initialization
        function enhancedInit() {
            try {
                // Initialize all systems with error handling
                initAudioContext();
                initEQKnobs();
                initPitchControl();
                initCrossfader();
                initTurntable();
                
                // Get postcard ID from URL
                const urlParams = new URLSearchParams(window.location.search);
                const id = parseInt(urlParams.get('id')) || 1;
                const index = postcards.findIndex(p => p.id === id);
                
                // Load the postcard
                loadPostcard(index >= 0 ? index : 0);
                
                // Generate QR codes with error handling
                try {
                    generateQRCodes();
                } catch (qrError) {
                    console.log('QR Code generation failed:', qrError);
                }
                
                // Event Listeners with null checks
                const nextBtn = document.getElementById('next-btn');
                const prevBtn = document.getElementById('prev-btn');
                const flipBtn = document.getElementById('flip-btn');
                const nextKnob = document.getElementById('next-knob');
                const prevKnob = document.getElementById('prev-knob');
                const shareBtn = document.getElementById('share-btn');
                const postcard = document.getElementById('postcard');
                const postcardInner = postcard ? postcard.querySelector('.postcard-inner') : null;
                
                if (nextBtn) nextBtn.addEventListener('click', nextPostcard);
                if (prevBtn) prevBtn.addEventListener('click', prevPostcard);
                if (flipBtn) flipBtn.addEventListener('click', flipPostcard);
                if (nextKnob) nextKnob.addEventListener('click', nextPostcard);
                if (prevKnob) prevKnob.addEventListener('click', prevPostcard);
                if (postcardInner) postcardInner.addEventListener('click', flipPostcard);
                
                // Share functionality
                if (shareBtn) {
                    shareBtn.addEventListener('click', async () => {
                        try {
                            const shareData = {
                                title: 'CrateJuice Sonic Postcard',
                                text: `Check out this sonic postcard: ${currentPostcard.frontTitle.replace('<br>', ' ')}`,
                                url: window.location.href
                            };
                            
                            if (navigator.share && /iPhone|iPad|iPod|Android/i.test(navigator.userAgent)) {
                                await navigator.share(shareData);
                            } else {
                                fallbackShare(shareData);
                            }
                        } catch (err) {
                            if (err.name !== 'AbortError') {
                                fallbackShare({
                                    title: 'CrateJuice Sonic Postcard',
                                    text: `Check out this sonic postcard: ${currentPostcard.frontTitle.replace('<br>', ' ')}`,
                                    url: window.location.href
                                });
                            }
                        }
                    });
                }
                
                // Keyboard navigation
                document.addEventListener('keydown', (e) => {
                    try {
                        switch(e.key) {
                            case 'ArrowRight':
                            case 'n':
                            case 'N':
                                e.preventDefault();
                                nextPostcard();
                                break;
                            case 'ArrowLeft':
                            case 'p':
                            case 'P':
                                e.preventDefault();
                                prevPostcard();
                                break;
                            case ' ':
                            case 'Enter':
                            case 'f':
                            case 'F':
                                e.preventDefault();
                                if (e.target.closest('.turntable-section')) {
                                    togglePlayback();
                                } else {
                                    flipPostcard();
                                }
                                break;
                        }
                    } catch (keyError) {
                        console.log('Keyboard event error:', keyError);
                    }
                });
                
                // Touch gestures for mobile
                if (postcard) {
                    let touchStartX = 0;
                    let touchEndX = 0;
                    
                    postcard.addEventListener('touchstart', (e) => {
                        touchStartX = e.changedTouches[0].screenX;
                    });
                    
                    postcard.addEventListener('touchend', (e) => {
                        touchEndX = e.changedTouches[0].screenX;
                        handleSwipe();
                    });
                    
                    function handleSwipe() {
                        const swipeThreshold = 50;
                        const diff = touchStartX - touchEndX;
                        
                        if (Math.abs(diff) > swipeThreshold) {
                            if (diff > 0) {
                                nextPostcard();
                            } else {
                                prevPostcard();
                            }
                        }
                    }
                }
                
                // Start VU meter simulation
                setTimeout(() => {
                    simulateVUMeters();
                }, 1000);
                
                // Set up viewport handling for iOS
                if (/iPhone|iPad|iPod/i.test(navigator.userAgent)) {
                    document.addEventListener('touchstart', () => {}, { passive: true });
                    
                    window.addEventListener('orientationchange', () => {
                        setTimeout(() => {
                            window.scrollTo(0, 0);
                        }, 500);
                    });
                }
                
            } catch (initError) {
                console.error('Initialization error:', initError);
                // Fallback: just show the basic postcard
                const loading = document.getElementById('loading');
                const postcard = document.getElementById('postcard');
                if (loading) loading.style.display = 'none';
                if (postcard) postcard.style.display = 'block';
            }
        }
        
        // Handle browser navigation
        window.addEventListener('popstate', () => {
            try {
                const urlParams = new URLSearchParams(window.location.search);
                const id = parseInt(urlParams.get('id')) || 1;
                const index = postcards.findIndex(p => p.id === id);
                
                if (index >= 0 && index !== currentIndex) {
                    loadPostcard(index);
                }
            } catch (popError) {
                console.log('Navigation error:', popError);
            }
        });
        
        // PWA Installation with error handling
        let deferredPrompt;
        
        window.addEventListener('beforeinstallprompt', (e) => {
            try {
                e.preventDefault();
                deferredPrompt = e;
                showInstallPrompt();
            } catch (installError) {
                console.log('Install prompt error:', installError);
            }
        });
        
        function showInstallPrompt() {
            if (!window.matchMedia('(display-mode: standalone)').matches) {
                const installBtn = document.createElement('button');
                installBtn.textContent = 'INSTALL APP';
                installBtn.className = 'action-btn';
                installBtn.style.marginLeft = '10px';
                
                installBtn.addEventListener('click', async () => {
                    try {
                        if (deferredPrompt) {
                            deferredPrompt.prompt();
                            const { outcome } = await deferredPrompt.userChoice;
                            
                            if (outcome === 'accepted') {
                                showToast('App installed successfully!');
                            }
                            deferredPrompt = null;
                            installBtn.remove();
                        }
                    } catch (installError) {
                        console.log('Installation error:', installError);
                    }
                });
                
                const actionButtons = document.querySelector('.action-buttons');
                if (actionButtons) {
                    actionButtons.appendChild(installBtn);
                }
            }
        }
        
        // Service Worker Registration with error handling
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                try {
                    const swCode = `
                    const CACHE_NAME = 'cratejuice-v1';
                    const urlsToCache = [
                        '/',
                        'https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&display=swap'
                    ];
                    self.addEventListener('install', (event) => {
                        event.waitUntil(
                            caches.open(CACHE_NAME)
                                .then((cache) => cache.addAll(urlsToCache))
                                .catch(err => console.log('Cache error:', err))
                        );
                    });
                    
                    self.addEventListener('fetch', (event) => {
                        event.respondWith(
                            caches.match(event.request)
                                .then((response) => response || fetch(event.request))
                                .catch(err => fetch(event.request))
                        );
                    });
                    `;
                    
                    const blob = new Blob([swCode], { type: 'application/javascript' });
                    const swUrl = URL.createObjectURL(blob);
                    
                    navigator.serviceWorker.register(swUrl)
                        .then((registration) => {
                            console.log('SW registered: ', registration);
                        })
                        .catch((registrationError) => {
                            console.log('SW registration failed: ', registrationError);
                        });
                } catch (swError) {
                    console.log('Service worker setup error:', swError);
                }
            });
        }
        
        // Start the app when DOM is ready
        document.addEventListener('DOMContentLoaded', enhancedInit);
    </script>
</body>
</html>