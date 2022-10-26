import { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useRouter } from "next/router";
import { login, reset_register_success } from "../actions/auth";
import Layout from "../components/hocs/Layout";
import Navbar from "../components/Navbar";
import { useForm } from "react-hook-form";
import Link from "next/link";

const LoginPage = () => {
  const dispatch = useDispatch();
  const router = useRouter();
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  useEffect(() => {
    if (dispatch && dispatch !== null && dispatch !== undefined)
      dispatch(reset_register_success());
  }, [dispatch]);

  const onSubmit = (data) => {
    if (dispatch && dispatch !== null && dispatch !== undefined)
      dispatch(login(data.username, data.password));
  };

  if (typeof window !== "undefined" && isAuthenticated) router.push(`/app/`);

  return (
    <Layout
      title="Kanban App | Login"
      content="Login page for kanban app login"
    >
      <Navbar />

      <div className="flex flex-col h-full">
        <div className="flex flex-col w-full p-6 m-auto sm:w-1/2 md:w-1/2 lg:w-1/2 my-28">
          <h2 className="mx-auto mb-10 text-3xl font-semibold">
            Welcome Back!
          </h2>
          <form onSubmit={handleSubmit(onSubmit)} className="w-full">
            <div className="mb-6">
              <label
                htmlFor="success"
                className="block mb-2 text-sm font-medium text-purple-primary"
              >
                Username
              </label>
              <input
                type="text"
                id="success"
                className="border border-grey-dark-primary text-grey-dark-primary placeholder-grey-light-tertiary text-sm rounded-lg focus:ring-purple-primary focus:border-purple-primary block w-full p-2.5"
                placeholder="Username"
                {...register("username", { required: true })}
              />
              <p className="mt-2 text-sm text-purple-primary">
                {errors.username && (
                  <span className="text-red-primary">
                    This field is required
                  </span>
                )}
              </p>
            </div>

            <div className="mb-6">
              <label
                htmlFor="password"
                className="block mb-2 text-sm font-medium text-purple-primary"
              >
                Password
              </label>
              <input
                type="password"
                id="password"
                className="border border-grey-dark-primary text-grey-dark-primary placeholder-grey-light-tertiary text-sm rounded-lg focus:ring-purple-primary focus:border-purple-primary block w-full p-2.5"
                placeholder="Password"
                {...register("password", { required: true })}
              />
              <p className="mt-2 text-sm text-purple-primary">
                {errors.password && (
                  <span className="text-red-primary">
                    This field is required
                  </span>
                )}
              </p>
            </div>
            <button className="bg-purple-primary hover:bg-purple-secondary text-white font-bold w-full py-2.5 rounded-lg">
              Login
            </button>
            <div className="flex justify-center mt-2 text-sm md:invisible">
              <h1 className="">Don't have an account? </h1>
              <Link href="/register">
                <a className="ml-1 font-bold text-purple-primary hover:underline">
                  Create Account
                </a>
              </Link>
            </div>
          </form>
        </div>
      </div>
    </Layout>
  );
};

export default LoginPage;
