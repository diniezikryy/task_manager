/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./node_modules/flowbite/**/*.js",
    "./src/pages/**/*.{js,ts,jsx,tsx}",
    "./src/components/**/*.{js,ts,jsx,tsx}",
    "node_modules/flowbite-react/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        body: ["Plus Jakarta Sans", "sans-serif"],
      },
      colors: {
        "purple-primary": "#635FC7",
        "purple-secondary": "#A8A4FF",
        "grey-dark-primary": "#000112",
        "grey-dark-secondary": "#20212C",
        "grey-dark-tertiary": "#2B2C37",
        "grey-dark-quartenary": "#3E3F4E",
        white: "#FFFFFF",
        "grey-light-primary": "#F4F7FD",
        "grey-light-secondary": "#E4EBFA",
        "grey-light-tertiary": "#828FA3",
        "red-primary": "#EA5555",
        "red-secondary": "#FF9898",
        test: "#979797",
        "dark-purple": "#081A51",
        "light-white": "rgba(255,255,255,0.18)",
      },
    },
  },
  plugins: [require("flowbite/plugin")],
};
