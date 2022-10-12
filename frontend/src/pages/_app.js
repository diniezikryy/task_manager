import "../styles/globals.css";
import "tailwindcss/tailwind.css";

import Head from "next/head";
import { Provider } from "react-redux";
import { useStore } from "../store";

const App = ({ Component, pageProps }) => {
  const store = useStore(pageProps.initialReduxState);

  return (
    <Provider store={store}>
      <Head>
        <title>HTTPOnly Auth</title>
        <meta name="viewport" content="width=device-width, inital-scale=1" />
      </Head>
      <Component {...pageProps} />
    </Provider>
  );
};

export default App;
