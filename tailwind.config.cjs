/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
	  extend: {
		fontSize: {
        '3xs': ['8px', { lineHeight: '1.5' }],
        '2xs': ['12px', { lineHeight: '1.5' }],
      },
	  },
	},
	darkMode: ["class", '[data-theme="dark"]'], // Permite alternar o tema via data-theme
	plugins: [require("@tailwindcss/typography"), require("daisyui")],
	daisyui: {
	  themes: ["dark", "light"],
	  darkTheme: "dark",
	  logs: false,
	},
  };
  