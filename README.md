```
# Chess.com Rating Display for Divoom Pixoo

## About The Project
This project is designed to fetch the Chess.com rating of a user and display it on a Divoom Pixoo 64x64 pixel LED display. It's perfect for chess enthusiasts who want a dynamic and visual representation of their chess rating. The script automatically updates the display with the latest rating at set intervals.

## Getting Started

### Prerequisites
- Python 3.x
- A Divoom Pixoo 64x64 pixel LED display
- Network connectivity between your Divoom Pixoo display and the device running the script

### Installation
1. Clone this repository:
```
git clone https://github.com/avollrath/chess-rating.git
cd chess-rating
```

2. Install required dependencies:
```
pip install -r requirements.txt
```

3. Setup environment variables by creating a `.env` file in the project root with your Chess.com username and Pixoo IP address:
```
CHESS_USERNAME=your_chess_username
PIXOO_IP_ADDRESS=your_pixoo_ip_address
```

### Usage
Run the script to start displaying your Chess.com rating on your Divoom Pixoo display:
```
python chess_stats.py
```

## Customization
You can customize the font size, text color, and refresh interval by modifying the `chess_stats.py` script.

## Special Thanks
Special thanks to `SomethingWithComputers` for the `pixoo` library, which made it possible to communicate with the Divoom Pixoo display effortlessly. This project utilizes the `pixoo` library to render the chess rating on the display. Check out the library [here](https://github.com/SomethingWithComputers/pixoo).

## Contributing
Contributions are welcome! If you have a suggestion that would make this better, please fork the repo and create a pull request.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Project Link: [https://github.com/avollrath/chess-rating](https://github.com/avollrath/chess-rating)
```
