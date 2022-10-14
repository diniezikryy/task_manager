import Head from "next/head";
import Layout from "../hocs/Layout";

const homePage = () => {
  return (
    <Layout title="Kanban App | Home" content="Home page for kanban app">
      <div>
        <Head>
          <title>Kanban App | Home</title>
          <meta
            name="viewport"
            content="initial-scale=1.0, width=device-width"
          />
        </Head>

        <div>
          <h1>Welcome to Kanban App</h1>
          <p>Login or create an account to use this app</p>
          <p>General description of webapp...</p>
        </div>
      </div>
    </Layout>
  );
};

export default homePage;
