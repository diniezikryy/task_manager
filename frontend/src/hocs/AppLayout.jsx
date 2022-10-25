import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { request_refresh, logout } from "../actions/auth";
import Head from "next/head";
import Link from "next/link";
import { Button, Navbar } from "flowbite-react";

const AppLayout = ({ title, content, children }) => {
  const user = useSelector((state) => state.auth.user);
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);

  const dispatch = useDispatch();

  const logoutHandler = () => {
    if (dispatch && dispatch !== null && dispatch !== undefined) {
      dispatch(logout());
    }
  };

  useEffect(() => {
    if (dispatch && dispatch !== null && dispatch !== undefined)
      dispatch(request_refresh());
  }, [dispatch]);

  return (
    <>
      <Head>
        <title>{title}</title>
        <meta name="description" content={content} />
      </Head>

      <Navbar fluid={true} rounded={true}>
        <Navbar.Brand href="https://flowbite.com/">
          <img
            src="https://flowbite.com/docs/images/logo.svg"
            className="h-6 mr-3 sm:h-9"
            alt="Kanban Logo"
          />
          <span className="self-center text-xl font-semibold whitespace-nowrap dark:text-white">
            Kanban App
          </span>
        </Navbar.Brand>
        <div className="flex items-center">
          {isAuthenticated ? (
            <Button className="bg-purple-primary" onClick={logoutHandler}>
              Logout
            </Button>
          ) : (
            <Link href="/login">
              <Button className="bg-purple-primary">Login</Button>
            </Link>
          )}
        </div>
      </Navbar>
      <div className="">{children}</div>
    </>
  );
};

AppLayout.defaultProps = {
  title: "Kanban App | ",
  content: "Kanban Task Manager",
};

export default AppLayout;
