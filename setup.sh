#!/bin/bash
echo "Ensure packages are installed:"
sudo apt-get install git

echo "Clone repositories:"
git clone https://github.com/zsteig/SpotifyFrame
cd SpotifyFrame

echo "Add fonts to system:"
sudo cp /fonts/GothamRounded-Bold.otf /usr/share/fonts/opentype/GothamRounded-Bold/GothamRounded-Bold.otf
sudo cp /fonts/GothamRounded-Book.otf /usr/share/fonts/opentype/GothamRounded-Book/GothamRounded-Book.otf

echo "Installing spotipy library"
pip install spotipy --upgrade

echo "Enter your Spotify Client ID:"
read spotify_client_id
export SPOTIPY_CLIENT_ID=$spotify_client_id

echo "Enter your Spotify Client Secret:"
read spotify_client_secret
export SPOTIPY_CLIENT_SECRET=$spotify_client_secret

echo "Enter your Spotify Redirect URI:"
read spotify_redirect_uri
export SPOTIPY_REDIRECT_URI=$spotify_redirect_uri

echo "Enter your spotify username:"
read spotify_username

python Python/generateToken.py $spotify_username

echo
echo "****** Spotify Token Created ******"
echo "Filename: .cache"

echo "Enter the full path to your spotify token:"
read spotify_token_path

install_path=$(pwd)

echo "Creating service to run SpotifyFrame on startup:"
install_path=$(pwd)
service_file="/etc/systemd/system/spotifyframe.service"

sudo touch $service_file

# Add service details to file
sudo bash -c 'cat <<EOF > '"$service_file"'
[Unit]
Description=Run main.py at startup
After=network.target

[Service]
ExecStart=/user/bin/python3 '"$install_path"'/Python/main.py ${spotify_username ${spotify_token_path}}
WorkingDirectory='"$install_path"'/Python
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
EOF'

# Enable and start the service
sudo systemctl daemon-reload
sudo systemctl enable spotifyframe.service
sudo systemctl start spotifyframe.service

echo "Service created and started. main.py will run on startup."
echo "SETUP IS COMPLETE"
