import {NextPage} from "next";
import {ReactNode} from "react";
import CommonHeader from "../Header";

type LayoutProps = {
    children: ReactNode
}

const Layout: NextPage<LayoutProps> = ({ children }) => {
    return (
        <>
            <CommonHeader />
            { children }
        </>
    )
}

export default Layout
