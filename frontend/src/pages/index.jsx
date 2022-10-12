import Head from "next/head";

const homePage = () => {
  return (
    <div>
      <Head>
        <title>Kanban App | Home</title>
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      </Head>

      <div>
        <h1>Welcome to Kanban App</h1>
        <p>Here will be a list of all your boards</p>
      </div>
    </div>
  );
};

export default homePage;
